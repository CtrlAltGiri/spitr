package routes

import (
	"spitr/beservice/controllers"

	"github.com/gin-gonic/gin"
)

func BarRoute(router *gin.Engine) {
	router.POST("/bar", controllers.CreateBar())
	router.GET("/bar/:barId", controllers.GetBar())
}
