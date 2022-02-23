import re

def scan_meter_tf(sent):
    skeleton = sent
    skeleton = re.sub(r'([kgjtdpbL]|\.[td])h', 'C', sent)  #有気音は子音1つ
    skeleton = re.sub('ch', 'CC', skeleton)  #硬口蓋の無声有気音は重子音
    skeleton = re.sub(r'[eo]\sa[aiu]', 'VW', skeleton)
    skeleton = re.sub(r'[eo]\sa', 'VV', skeleton)
    skeleton = re.sub(r'aa|ii|uu|[eo]|\.\.rr|\.\.ll', 'W',skeleton)  # aiu の長音、eo,
    skeleton = re.sub('ai|au', 'W', skeleton)  #二重母音
    skeleton = re.sub('a;i|a;u', 'W', skeleton)  #二重母音のアクセント表記がこれになっているのがあったので
    skeleton = re.sub(r'[aiu\']|\.[rl]', 'V', skeleton)  #短母音
    skeleton = re.sub(r'[kgcjtdnpbmsyrlvhmH]|:n|\.[tdnshm]|;[nsm]', 'C',skeleton)  #子音
    skeleton = re.sub(r'\s', '', skeleton)
    skeleton = re.sub(';', '', skeleton)  #udattaを取り除く
    skeleton = re.sub(':', '', skeleton)  #svaritaを取り除く
    meter = re.sub('W|VC{2,}', 'H', skeleton)  #長母音二重母音または短母音と2つ以上の子音は重い
    meter = re.sub('VC$', 'H', meter)  #短母音と1つの子音で終わると重い
    meter = re.sub('V', 'L', meter)  # 残った単母音は軽い
    meter = re.sub('C', '', meter)  # 他の子音は考えなくて良い
    return meter, skeleton


def scan_meter_tsu(sent):
    skeleton = sent
    skeleton = re.sub(';', '', skeleton)  #udattaを取り除く
    skeleton = re.sub(':', '', skeleton)  #svaritaを取り除く
    skeleton = re.sub(r'[eo]\sa[aiu]', 'VW', skeleton)
    skeleton = re.sub(r'[eo]\sa', 'VV', skeleton)
    skeleton = re.sub(r'[AIUQeoEO]', 'W',skeleton)  # 長母音、二重母音
    skeleton = re.sub(r'[aiuqL\']', 'V', skeleton)  #短母音(avagraha含む)
    skeleton = re.sub(r'[kKgGVcCjJYwWxXNtTdDnpPbBmyrlvzSshMHfF]|:n|\.[tdnshm]|;[nsm]', 'C',skeleton)  #子音
    skeleton = re.sub(r'\s', '', skeleton)
    meter = re.sub('W|VC{2,}', '_', skeleton)  #長母音二重母音または短母音と2つ以上の子音は重い
    meter = re.sub('VC$', '_', meter)  #短母音と1つの子音で終わると重い
    meter = re.sub('V', 'u', meter)  # 残った単母音は軽い
    meter = re.sub('C', '', meter)  # 他の子音は考えなくて良い
    return meter, skeleton

class meterScanner:
    sentence = None

    def __init__(self, sentence):
        self.sent = sentence
        self.meter = ''
        self.skeleton = ''

    def scanTF(self):
        skeleton = self.sent
        skeleton = re.sub(r'([kgjtdpbL]|\.[td])h', 'C', skeleton)  #有気音は子音1つ
        skeleton = re.sub('ch', 'CC', skeleton)  #硬口蓋の無声有気音は重子音
        skeleton = re.sub(r'[eo]\sa[aiu]', 'VW', skeleton)
        skeleton = re.sub(r'[eo]\sa', 'VV', skeleton)
        skeleton = re.sub(r'aa|ii|uu|[eo]|\.\.rr|\.\.ll', 'W',skeleton)  # aiu の長音、eo,
        skeleton = re.sub('ai|au', 'W', skeleton)  #二重母音
        skeleton = re.sub('a;i|a;u', 'W', skeleton)  #二重母音のアクセント表記がこれになっているのがあったので
        skeleton = re.sub(r'[aiu\']|\.[rl]', 'V', skeleton)  #短母音
        skeleton = re.sub(r'[kgcjtdnpbmsyrlvhmH]|:n|\.[tdnshm]|;[nsm]', 'C',skeleton)  #子音
        skeleton = re.sub(r'\s', '', skeleton)
        skeleton = re.sub(';', '', skeleton)  #udattaを取り除く
        skeleton = re.sub(':', '', skeleton)  #svaritaを取り除く
        meter = re.sub('W|VC{2,}', 'H', skeleton)  #長母音二重母音または短母音と2つ以上の子音は重い
        meter = re.sub('VC$', 'H', meter)  #短母音と1つの子音で終わると重い
        meter = re.sub('V', 'L', meter)  # 残った単母音は軽い
        meter = re.sub('C', '', meter)  # 他の子音は考えなくて良い

        self.meter = meter
        self.skeleton = skeleton
    
    
    def scanTSU(self):
        skeleton = self.sent
        skeleton = re.sub(';', '', skeleton)  #udattaを取り除く
        skeleton = re.sub(':', '', skeleton)  #svaritaを取り除く
        skeleton = re.sub(r'[kKgGVcCjJYwWxXNtTdDnpPbBmyrlvzSshMHfF]', 'C',skeleton)  #子音
        skeleton = re.sub(r'[eo]\sa[aiu]', 'VW', skeleton) #短を V, 長を W とする
        skeleton = re.sub(r'[eo]\sa', 'V', skeleton)
        skeleton = re.sub(r'[AIUQeoEO]', 'W',skeleton)  # 長母音、二重母音
        skeleton = re.sub(r'[aiuqL\']', 'V', skeleton)  #短母音(avagraha含む)
        skeleton = re.sub(r'\s', '', skeleton)
        meter = re.sub('W|VC{2,}', '_', skeleton)  #長母音二重母音または短母音と2つ以上の子音は重い
        meter = re.sub('VC$', '_', meter)  #短母音と1つの子音で終わると重い
        meter = re.sub('V', 'u', meter)  # 残った単母音は軽い
        meter = re.sub('C', '', meter)  # 他の子音は考えなくて良い

        self.meter = meter
        self.skeleton = skeleton


# sent = 'agn;im IDe'
# scanner = meterScanner(sent)
# scanner.scanTSU()
# met = scanner.meter
# sklt = scanner.skeleton
# print(met)
# print(sklt)