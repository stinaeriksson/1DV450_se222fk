# encoding: utf-8
class Project < ActiveRecord::Base
  attr_accessible :name, :description, :start_date, :end_date, :owner_id, :user_id, :user_ids
  has_many :tickets, :dependent => :destroy
  has_and_belongs_to_many :users

  validates :name, 
  			:presence => {:message => "Du måste ange ett namn"},
  			:length => {:minimum => 3, :message => "Namnet måste vara minst 3 tecken"},
        :uniqueness => {:message => "Det finns redan ett projekt med samma namn, vänligen ändra namnet."}


  validates :description,
  			:presence => {:message => "Du måste ange en beskrivning"}

  validates :start_date,
        :presence => {:message => "Du måste ange ett startdatum"}

  validates :end_date,
        :presence => {:message => "Du måste ange ett slutdatum"}


end
