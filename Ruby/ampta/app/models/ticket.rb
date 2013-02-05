class Ticket < ActiveRecord::Base
  attr_accessible :name, :description, :user_id, :project_id, :status_id
  belongs_to :user
  belongs_to :status
  belongs_to :project

end
