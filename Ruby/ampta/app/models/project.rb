# encoding: utf-8

class Project < ActiveRecord::Base
  attr_accessible :name, :description, :start_date, :end_date
  has_many :tickets
  has_and_belongs_to_many :users
  belongs_to :user

  validates :name, 
  			:presence => {:message => "Du måste ange ett namn"},
  			:length => {:minimum => 3, :message => "Namnet måste vara minst 3 tecken"}

  validates :description,
  			:presence => {:message => "Du måste ange en beskrivning"}

  validates :start_date,
  			:presence => {:message => "Du måste ange ett startdatum"}

  validates :end_date,
  			:presence => {:message => "Du måste ange ett slutdatum"}

  validate :start_date_valid

  validate :end_date_valid

  private

  def start_date_valid
    if !start_date.is_a?(Date)
      errors.add(:start_date, 'Datum angivet i fel format') 
    end
  end

  private

  def end_date_valid
    if !end_date.is_a?(Date)
      errors.add(:end_date, 'Datum angivet i fel format') 
    end
  end


end
