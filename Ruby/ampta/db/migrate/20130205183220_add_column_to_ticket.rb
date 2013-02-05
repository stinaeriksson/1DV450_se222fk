class AddColumnToTicket < ActiveRecord::Migration
  def change
  	add_column :tickets, :start_time, :datetime
  	add_column :tickets, :end_time, :datetime
  end
end
