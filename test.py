import re

txt = "  2:22:55 5 N/A  1  accept gw-850899 < eth1  LogId: 0; ContextNum: <max_null>; OriginSicName: cn=cp_mgmt,o=gw-850899..ujrk2f; OriginSicName: cn=cp_mgmt,o=gw-850899..ujrk2f; HighLevelLogKey: 18446744073709551615; inzone: Local; outzone: Internal; service_id: CPD_amon; src: 192.168.1.208; dst: gw-850899; proto: tcp; UP_match_table: TABLE_START; ROW_START: 0; match_id: 1; layer_uuid: 1549c7b1-7b5f-42f1-82f8-c7b4688f6476; layer_name: Network; rule_uid: 1583bf02-6859-4cf6-817f-44f3b3482431; rule_name: Cleanup rule; action: 2; parent_rule: 0; ROW_END: 0; UP_match_table: TABLE_END; ProductName: VPN-1 & FireWall-1; svc: CPD_amon; sport_svc: 34750; ProductFamily: Network;"
#Find all lower case characters alphabetically between "a" and "m":
x = txt.split(';')
print(x[9])