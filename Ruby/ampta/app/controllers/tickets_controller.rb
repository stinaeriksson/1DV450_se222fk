# encoding: utf-8
class TicketsController < ApplicationController
	before_filter :authenticate_user, :home
	before_filter :control_user_new, :only =>[:new, :update]
	before_filter :control_user_show, :only => [:show]

	def index
			
	end

	def show
		@ticket = Ticket.find(params[:id])
		@id = @ticket.status_id;
		@status = Status.where("id = ?", @id)
		@status_name = @status.first.status_name

		@user_id = @ticket.user_id;
		@user = User.where("id = ?", @user_id)
		@first_name = @user.first.first_name
		@last_name = @user.first.last_name
	end

	def destroy
		@id = @current_user.id
		@ticket = Ticket.find(params[:id])
		@user_id = @ticket.user_id
		@project = @ticket.project_id
		
		if @id == @user_id
			@ticket = Ticket.find(params[:id])
			@ticket.destroy
			flash[:notice] = "Ticket borttagen"
			redirect_to :action => "show", :controller => "projects", :id => @project
		else
			flash[:notice] = "Du har ej rättigheter att ta bort ticket"
			redirect_to :action => "show", :id => @ticket.id
		end

	end

	def new
		@user_id = @current_user.id
		@project = params[:id]
		@ticket = Ticket.new
	end

	def create
		@user_id = @current_user.id
		@ticket = Ticket.new(params[:ticket])
		
		if @ticket.save
			flash[:notice] = "Ticket skapad!"
			redirect_to :action => "show", :id => @ticket.id
		else
			@project = params[:ticket][:id]
			render :action => "new", :project_id => @project
			
		end
		
	end

	def edit
		@id = @current_user.id
		@ticket = Ticket.find(params[:id])
		@user_id = @ticket.user_id
		@project_id = @ticket.project_id

		case
			when @project_id == @current_user.projects.find_by_id(@project_id)
				return true

			when @id == @user_id
				return true
					
			else
					
			flash[:notice] = "Du har ej rättigheter att redigera ticket"
			redirect_to :action => "show", :id => @ticket.id
			
		end  
	end

	def update
		@ticket = Ticket.find(params[:id])
		if @ticket.update_attributes(params[:ticket])
			flash[:notice] = "Ticket uppdaterad!"
			redirect_to ticket_path
		else
			render :action => "edit"
		end
	end

end
