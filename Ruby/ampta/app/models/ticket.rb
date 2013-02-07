class Ticket < ActiveRecord::Base
  attr_accessible :name, :description
  belongs_to :user
  belongs_to :status
  belongs_to :project

end
