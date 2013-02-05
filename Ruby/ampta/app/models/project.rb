class Project < ActiveRecord::Base
  attr_accessible :name, :description, :start_date, :end_date, :owner_id
  has_many :tickets
  has_and_belongs_to_many :users
  belongs_to :user
end
