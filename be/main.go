package main

import (
	"spitr/beservice/config"
	"spitr/beservice/routes"

	"github.com/gin-gonic/gin"
)

func main() {
	router := gin.Default()
	config.ConnectDB()

	routes.BarRoute(router)
	router.Run("localhost:6000")
}
