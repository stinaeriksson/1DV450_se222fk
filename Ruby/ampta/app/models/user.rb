class User < ActiveRecord::Base
  # attr_accessible :title, :body
  has_many :tickets
  has_and_belongs_to_many :projects
end
