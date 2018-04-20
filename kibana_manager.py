import json
import elasticsearch

'''attempts to connect to passed elasticsearch address. If connection is
	successful the es object is returned'''
def connect_to_es(es_address, username=None, password=None):

    try:
	es = elasticsearch.Elasticsearch(es_address)

    except:
	print("Connection to elasticsearch at " + str(es_address) + " failed.")
        es = None


    return es

'''updates existing dashboard object that is pre-indexed in elasticsearch with a 
	new panel'''
def insert_panel_into_dashboard(panel, dashboard_id, es_index):
    



'''returns created panel JSON for future Kibana indexing. Allows ease of 
	panel creation'''
def create_panel(panel_id, panel_type, title, vis_type, params, aggs, ui_state=None, search_source=None,version=1,description=None,listeners=None):
    
    panel = {
        "_id": panel_id,
	"_type": panel_type,
	"_source":{
		"visState": create_visState(title, vis_type, params, aggs),
		"description": description,
		"title": title,
		"uiStateJSON": create_uiState(ui_state),
		"version": version,
		"kibanaSavedObjectMeta":{
			"searchSourceJSON": create_searchSource(search_source)	
	  }

	}
      }

    return json.dumps(panel)


'''creates required visState string for use during the creation of 
	a panel as it is a required field:value for elastic specific schema'''
def create_visState(title, vis_type, params, aggs=None, listeners=None):

    visState = {
	"title": title,
	"type": vis_type,
	"params": params,
	"aggs": create_aggs(aggs),
	"listeners": listeners
     }

    return str(visState)

'''creates a savedSearch string '''
def create_savedSearch():

    savedSearch = {
            '''MOST FOCUS NEEDS TO BE IN HERE'''
     
     }

    return str(savedSearch)

''''''
def create_uiState():

    uiState = {



     }

    return str(uiState)









