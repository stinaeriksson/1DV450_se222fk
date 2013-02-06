# encoding: utf-8
# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rake db:seed (or created alongside the db with db:setup).
#
# Examples:
#
#   cities = City.create([{ name: 'Chicago' }, { name: 'Copenhagen' }])
#   Mayor.create(name: 'Emanuel', city: cities.first)



t2 = Ticket.create(:name => "anotherTicket", :description => "Här kommer en liten another beskrivning", :user_id => 1, :project_id => 2, :status_id => 1)
p1 = Project.create(:name => "anotherProject", :description => "Här kommer en liten another beskrivning", :start_date => "12/02/2013", :end_date => "29/02/2013", :owner_id => 1)
p2 = Project.create(:name => "SuperProjektet", :description => " beskrivning jaaaaaa", :start_date => "12/02/2013", :end_date => "12/06/2013", :owner_id => 2)

p2.tickets << t2