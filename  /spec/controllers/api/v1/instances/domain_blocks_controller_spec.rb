# frozen_string_literal: true

require 'rails_helper'

describe Api::V1::Instances::DomainBlocksController do
  render_views

  describe 'GET #index' do
    it 'returns http success' do
      Setting.show_domain_blocks = 'all'
      get :index

      expect(response).to have_http_status(200)
    end
  end
end
