class TicketsController < ApplicationController

	def index
		@tickets_for_user = Ticket.where(["user_id = ?", "1"]) 
	end

	def show
		@ticket = Ticket.find(params[:id])
	end

	def destroy
		@ticket = Ticket.find(params[:id])
		@ticket.destroy
		redirect_to tickets_path
	end
end
