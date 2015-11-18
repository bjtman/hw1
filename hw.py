import mediacloud, datetime 

mc = mediacloud.api.MediaCloud('API_KEY')

res = mc.sentenceCount('(democratic)', solr_filter=[mc.publish_date_query( datetime.date( 2014, 5, 5), datetime.date( 2015, 5, 5) ), 'media_sets_id:1' ])
res2 = mc.sentenceCount('(republican)', solr_filter=[mc.publish_date_query( datetime.date( 2014, 5, 5), datetime.date( 2015, 5, 5) ), 'media_sets_id:1' ])
print res['count']
print res2['count']