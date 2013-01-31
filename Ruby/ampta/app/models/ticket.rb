class Ticket < ActiveRecord::Base
  # attr_accessible :title, :body
  belongs_to :user, :status, :projekt
end
