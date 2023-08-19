package models

import "go.mongodb.org/mongo-driver/bson/primitive"

type Bar struct {
	Id          primitive.ObjectID `json:"Id, omitempty`
	Bar         string             `json:"bar,omitempty", validate:"required"`
	UserId      string             `json:"userId, omitempty", validate:"required"`
	DisplayName string             `json:"displayName, omitempty", validate:"required"`
}
