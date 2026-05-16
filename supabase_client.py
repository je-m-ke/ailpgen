from supabase import create_client

url = "https://artjvcoqftopdcwgffsm.supabase.co/rest/v1/"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFydGp2Y29xZnRvcGRjd2dmZnNtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzg5MTQ1MTcsImV4cCI6MjA5NDQ5MDUxN30.FEZt7tUR0TxXccc943FFkdkoe_1PwI_Ku7h68mOhzyM"

supabase = create_client(url, key)