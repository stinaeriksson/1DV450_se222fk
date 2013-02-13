# encoding: utf-8
class TicketsController < ApplicationController
	before_filter :authenticate_user, :only => [:create, :edit]
	def index
			
	end

	def show
		@ticket = Ticket.find(params[:id])
		
	end

	def destroy
		@ticket = Ticket.find(params[:id])
		@ticket.destroy
		redirect_to :root

	end

	def new
		@ticket = Ticket.new
	end

	def create
		@ticket = Ticket.new(params[:ticket])
		
		if @ticket.save
			redirect_to :action => "show", :id => @ticket.id
		else
			render :action => "new"
		end
	end

	def edit
		@id = @current_user.id
		@ticket = Ticket.find(params[:id])
		@pid = @ticket.user_id
		
		unless @id == @pid
			
			flash[:notice] = "Du har ej rättigheter att redigera ticket"
			redirect_to :action => "show", :id => @ticket.id
			
		end

	end

	def update
		@ticket = Ticket.find(params[:id])
		if @ticket.update_attributes(params[:ticket])
			flash[:notice] = "Ticket uppdaterat!"
			redirect_to ticket_path
		else
			render :action => "edit"
		end
	end
end
