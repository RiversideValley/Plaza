# frozen_string_literal: true

Fabricator(:account_note) do
  account
  target_account { Fabricate(:account) }
  comment        'User note text'
end
