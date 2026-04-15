from requests import Session

class WhiskyHunter:
	def __init__(self) -> None:
		self.api = "https://whiskyhunter.net/api"
		self.session = Session()
		self.session.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
		}

	def _get(self, endpoint: str) -> dict:
		return self.session.get(f"{self.api}{endpoint}").json()
	
	def read_auction_data(self, slug: str) -> dict:
		return self._get(
			f"/auction_data/{slug}/auction_data_read")
	
	def get_auctions_data(self) -> dict:
		return self._get("/auctions_data/auctions_data_list")
	
	def get_auctions_info(self) -> dict:
		return self._get("/auctions_info/auctions_info_list")
	
	def get_distilleries_info(self) -> dict:
		return self._get("/distilleries_info/distilleries_info_list")
	
	def read_distillery_data(self, slug: str) -> dict:
		return self._get(
			f"/distillery_data/{slug}/distillery_data_read")
