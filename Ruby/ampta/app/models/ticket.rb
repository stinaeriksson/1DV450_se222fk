# encoding: utf-8
class Ticket < ActiveRecord::Base
  attr_accessible :name, :description, :status_id, :start_time, :end_time, :user_id, :project_id
  belongs_to :user
  belongs_to :status
  belongs_to :project


  validates :name, 
  			:presence => {:message => "Du måste ange ett namn"},
  			:length => {:minimum => 3, :message => "Namnet måste vara minst 3 tecken"}

  validates :description,
  			:presence => {:message => "Du måste ange en beskrivning"}

  

end
