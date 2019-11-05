from facebook_business.api import FacebookAdsApi
from facebook_business import adobjects
from facebook_business.adobjects.adaccountuser import AdAccountUser
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adsinsights import AdsInsights
from facebook_business.adobjects.adreportrun import AdReportRun
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.adspixel import AdsPixel
import json
import os 
os.chdir('D:/')

#Initialize a new Session and instantiate an API object:
token = 'EAAT9nrbCKZCEBAKggSzgIRsWJGyiV0zr4E7jiELswCUIAfVrYjubvUkvss7tiIa13At53qPBkdwJQXIH8YNpPzoswZCa6AgSZAT1Wmn6Y06CJfsZC2sKqy9JdO9na3TYFb1wkIlAV8kBSTKwX5uITBTCs5Tlg9yrsNuKGPp7HQZDZD'

my_app_id = '1404758019681265'
my_app_secret = '080a4d1b30e4e292518857f2e3ed4b1b'
my_access_token = token 
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
my_account = AdAccount('act_185955978120372')

# campaigns = my_account.get_campaigns()
# print(campaigns)

result = my_account.get_insights(params={'date_preset'   :'lifetime',
                                         'level'         :'ad'},

                                fields = [AdsInsights.Field.account_id,
                                        AdsInsights.Field.account_name,
                                        AdsInsights.Field.action_values,
                                        AdsInsights.Field.actions,
                                        AdsInsights.Field.ad_id,
                                        AdsInsights.Field.ad_name,
                                        AdsInsights.Field.adset_id,
                                        AdsInsights.Field.adset_name,
                                        # AdsInsights.Field.app_store_clicks,
                                        AdsInsights.Field.buying_type,
                                        AdsInsights.Field.campaign_id,
                                        AdsInsights.Field.campaign_name,
                                        AdsInsights.Field.canvas_avg_view_percent,
                                        AdsInsights.Field.canvas_avg_view_time,
                                        AdsInsights.Field.clicks,
                                        AdsInsights.Field.conversion_rate_ranking,
                                        AdsInsights.Field.conversion_values,
                                        AdsInsights.Field.conversions,
                                        AdsInsights.Field.cost_per_action_type,
                                        AdsInsights.Field.cost_per_conversion,
                                        AdsInsights.Field.cost_per_estimated_ad_recallers,
                                        AdsInsights.Field.cost_per_inline_link_click,
                                        AdsInsights.Field.cost_per_inline_post_engagement,
                                        AdsInsights.Field.cost_per_outbound_click,
                                        AdsInsights.Field.cost_per_thruplay,
                                        AdsInsights.Field.cost_per_unique_action_type,
                                        AdsInsights.Field.cost_per_unique_click,
                                        AdsInsights.Field.cost_per_unique_inline_link_click,
                                        AdsInsights.Field.cost_per_unique_outbound_click,
                                        AdsInsights.Field.cpc,
                                        AdsInsights.Field.cpm,
                                        AdsInsights.Field.cpp,
                                        AdsInsights.Field.ctr,
                                        AdsInsights.Field.date_start,
                                        AdsInsights.Field.date_stop,
                                        # AdsInsights.Field.deeplink_clicks,
                                        AdsInsights.Field.engagement_rate_ranking,
                                        AdsInsights.Field.estimated_ad_recall_rate,
                                        AdsInsights.Field.estimated_ad_recallers,
                                        AdsInsights.Field.frequency,
                                        AdsInsights.Field.full_view_impressions,
                                        AdsInsights.Field.full_view_reach,
                                        AdsInsights.Field.impressions,
                                        AdsInsights.Field.inline_link_click_ctr,
                                        AdsInsights.Field.inline_link_clicks,
                                        AdsInsights.Field.inline_post_engagement,
                                        AdsInsights.Field.instant_experience_clicks_to_open,
                                        AdsInsights.Field.instant_experience_clicks_to_start,
                                        AdsInsights.Field.instant_experience_outbound_clicks,
                                        AdsInsights.Field.mobile_app_purchase_roas,
                                        # AdsInsights.Field.newsfeed_avg_position,
                                        # AdsInsights.Field.newsfeed_clicks,
                                        # AdsInsights.Field.newsfeed_impressions,
                                        AdsInsights.Field.objective,
                                        AdsInsights.Field.outbound_clicks,
                                        AdsInsights.Field.outbound_clicks_ctr,
                                        AdsInsights.Field.purchase_roas,
                                        AdsInsights.Field.quality_ranking,
                                        AdsInsights.Field.reach,
                                        AdsInsights.Field.social_spend,
                                        AdsInsights.Field.spend,
                                        AdsInsights.Field.unique_actions,
                                        AdsInsights.Field.unique_clicks,
                                        AdsInsights.Field.unique_ctr,
                                        # AdsInsights.Field.unique_impressions,
                                        AdsInsights.Field.unique_inline_link_click_ctr,
                                        AdsInsights.Field.unique_inline_link_clicks,
                                        AdsInsights.Field.unique_link_clicks_ctr,
                                        AdsInsights.Field.unique_outbound_clicks,
                                        AdsInsights.Field.unique_outbound_clicks_ctr,
                                        AdsInsights.Field.video_30_sec_watched_actions,
                                        AdsInsights.Field.video_avg_time_watched_actions,
                                        # AdsInsights.Field.video_complete_watched_actions,
                                        AdsInsights.Field.video_p100_watched_actions,
                                        AdsInsights.Field.video_p25_watched_actions,
                                        AdsInsights.Field.video_p50_watched_actions,
                                        AdsInsights.Field.video_p75_watched_actions,
                                        AdsInsights.Field.video_p95_watched_actions,
                                        AdsInsights.Field.video_play_actions,
                                        AdsInsights.Field.video_play_curve_actions,
                                        AdsInsights.Field.video_thruplay_watched_actions,
                                        # AdsInsights.Field.website_clicks,
                                        AdsInsights.Field.website_ctr,
                                        AdsInsights.Field.website_purchase_roas])

# txt = json.dumps(str(result)[1:-1].split('<AdsInsights>')[1])

# file_facebook_ads = open("facebook.txt","w")
# file_facebook_ads.write(str(result))  
# file_facebook_ads.close()

# json.loads(result[0])

# for i in result[0]:
#         print(result[0][i])

# file1 = open("facebook.txt","r+")  
# print(file1.read())
# file1.close() 
result

AdsPixel.export_data


