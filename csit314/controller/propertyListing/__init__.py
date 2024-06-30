from .AgentCreatePropertyListingController import AgentCreatePropertyListingController
from .AgentEditPropertyListingController import AgentEditPropertyListingController
from .AgentRemovePropertyListingController import AgentRemovePropertyListingController
from .ViewPropertyListingController import ViewPropertyListingController
from .BuyerViewOldPropertyListingController import BuyerViewOldPropertyListingController
from .SearchPropertyListingController import SearchPropertyListingController

agent_create_property_listing_controller = AgentCreatePropertyListingController(name="AgentCreatePropertyListingController", import_name=__name__)
agent_edit_property_listing_controller = AgentEditPropertyListingController(name="AgentEditPropertyListingController", import_name=__name__)
agent_remove_property_listing_controller = AgentRemovePropertyListingController(name="AgentRemovePropertyListingController", import_name=__name__)
view_property_listing_controller = ViewPropertyListingController(name="ViewPropertyListingController", import_name=__name__)
buyer_view_old_property_listing_controller = BuyerViewOldPropertyListingController(name="BuyerViewOldPropertyListingController", import_name=__name__)
search_property_listing_controller = SearchPropertyListingController(name="SearchPropertyListingController", import_name=__name__)



