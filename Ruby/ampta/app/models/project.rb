class Project < ActiveRecord::Base
  # attr_accessible :title, :body
  has_many :ticket
  has_and_belongs_to_many :users
end
