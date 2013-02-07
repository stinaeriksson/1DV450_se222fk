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

	def new
		@ticket = Ticket.new
	end

	def create
		@ticket = Ticket.new(params[:ticket])

		if @ticket.save
			redirect_to tickets_path
		else
			render :action => "new"
		end
	end
end
