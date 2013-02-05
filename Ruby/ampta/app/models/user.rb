class User < ActiveRecord::Base
  attr_accessible :first_name, :last_name, :email, :password
  has_many :tickets
  has_many :projects
  has_and_belongs_to_many :projects
end
