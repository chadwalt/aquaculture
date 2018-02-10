from flask import Flask, jsonify
from models.py import Fish, Feed, Supplier
from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy
from instance.config import app_config
import os
from __init__ import app


class Fish(Resource):
    def get_fish(self, feed_name):
        fish_list = []
        fish_that_eat_feed = Fish.query.filter_by(feed_name=feed_name).all()
        if fish_that_eat_feed:
            for fish in fish_that_eat_feed:
                fish_details = {
                    'name': fish.name,
                    'id' : fish.id
                    }
                fish_list.append(fish_details)
            return jsonify({'fish that eat feed are': fish_list}, 200)
        else:
            return("no fish that eat that feed at the moment!")


class Feeds(Fish):
    
    @app.route('/<feed_name>')
    def get_feed(self, feed_name):
        feed_name = Feed.query.filter_by(name=feed_name).first()
        if feed_name:
            impact = Feed.query.filter_by(feed_name=feed_name).first()
            suppliers = get_supliers.feed_suppliers
            feed_id = Feed.query.filter_by(feed_name=feed_name).first()
            Fishes = Fish.Fish_list
        else:
            return("no feeds by that name yet!")

    def get_suppliers(self, feed_name):
        feed_suppliers = []
        suppliers = Supplier.query.filter_by(feed_name=feed_name).all()
        if suppliers:
            for supplier in suppliers:
                supplier_details = {
                    'id': supplier.id,
                    'name': supplier.name,
                    'telephone': supplier.telephone,
                    'price': supplier.price, # bug from database models
                    'feed_id': supplier.feed_id
                }
                feed_suppliers.append(supplier_details)

            return jsonify({'suppliers': feed_suppliers}, 200)
        else:
            return("no suppliers for that at the moment!")






