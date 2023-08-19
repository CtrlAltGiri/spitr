package controllers

import (
	"context"
	"fmt"
	"net/http"
	"spitr/beservice/config"
	"spitr/beservice/models"
	"spitr/beservice/responses"
	"time"

	"github.com/gin-gonic/gin"
	"github.com/go-playground/validator/v10"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/bson/primitive"
	"go.mongodb.org/mongo-driver/mongo"
)

var barCollection *mongo.Collection = config.GetCollection(config.DB, "bars")
var validate = validator.New()

func CreateBar() gin.HandlerFunc {
	return func(c *gin.Context) {
		ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
		var bar models.Bar
		defer cancel()

		//validate the request body
		if err := c.BindJSON(&bar); err != nil {
			c.JSON(http.StatusBadRequest, responses.BarResponse{Status: http.StatusBadRequest, Message: "error", Data: map[string]interface{}{"data": err.Error()}})
			return
		}

		//use the validator library to validate required fields
		if validationErr := validate.Struct(&bar); validationErr != nil {
			c.JSON(http.StatusBadRequest, responses.BarResponse{Status: http.StatusBadRequest, Message: "error", Data: map[string]interface{}{"data": validationErr.Error()}})
			return
		}

		newBar := models.Bar{
			Id:          primitive.NewObjectID(),
			Bar:         bar.Bar,
			UserId:      bar.UserId,
			DisplayName: bar.DisplayName,
		}

		result, err := barCollection.InsertOne(ctx, newBar)
		if err != nil {
			c.JSON(http.StatusInternalServerError, responses.BarResponse{Status: http.StatusInternalServerError, Message: "error", Data: map[string]interface{}{"data": err.Error()}})
			return
		}

		c.JSON(http.StatusCreated, responses.BarResponse{Status: http.StatusCreated, Message: "success", Data: map[string]interface{}{"data": result}})
	}
}

func GetBar() gin.HandlerFunc {
	return func(c *gin.Context) {
		ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
		barId := c.Param("barId")
		fmt.Println(barId)
		var bar models.Bar
		defer cancel()

		objId, _ := primitive.ObjectIDFromHex(barId)
		fmt.Println(objId)

		var bars []models.Bar
		results, err := barCollection.Find(ctx, bson.M{})
		defer results.Close(ctx)
		for results.Next(ctx) {
			var singleUser models.Bar
			if err = results.Decode(&singleUser); err != nil {
				c.JSON(http.StatusInternalServerError, responses.BarResponse{Status: http.StatusInternalServerError, Message: "error", Data: map[string]interface{}{"data": err.Error()}})
			}

			bars = append(bars, singleUser)
		}
		fmt.Println(bars)

		err = barCollection.FindOne(ctx, bson.M{"id": objId}).Decode(&bar)
		if err != nil {
			c.JSON(http.StatusInternalServerError, responses.BarResponse{Status: http.StatusInternalServerError, Message: "error", Data: map[string]interface{}{"data": err.Error()}})
			return
		}

		c.JSON(http.StatusOK, responses.BarResponse{Status: http.StatusOK, Message: "success", Data: map[string]interface{}{"data": bar}})
	}
}
