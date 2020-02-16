from auto import *
from pprint import pprint as pp
from cihai.core import Cihai
c=Cihai()
# c.unihan.bootstrap({})

"""
造zào - create/make
话huà - speaking
辶 - radical - zǒu zhī páng (Chuò) - indicates motion
福fú - blessing
福fú - blessing
礻 - radical - shì - show reveal.
神shén - god.
一yī - one
口kǒu - mouth
田tián - field (garden)

造zào - create/make
話huà - speaking
辶 - radical 162 - zǒu zhī páng - walk/walking (indicates motion)
福fú - blessing
礻- radical 113 - shì (cult), represents 示Shì - reveal, manifest; demonstrate
神shén - god.
一yī - one
口kǒu - mouth
田tián - field (garden)
園yuán - garden
土tǔ - earth/clay
口kǒu - mouth
亻rén - radical (man)
人rén - man
女nǚ - woman
囗wéi radical - imports

禁jìn - ban prohibit forbid.
示shì -  show/reveal
木mù - tree

魔mó - tempter
田tián - field (garden)
儿er - child
厶sī - secret (radical 28)
鬼guǐ - ghost, devil
木mù - tree
广guǎng - radical 53. wide, broad, expansive

婪lán - avaricious
女nǚ - woman
木mù - tree

困kùn - to surround, beseige; to be surrounded; difficult
木mù - tree
囗wéi - enclosure



"""

db=Cihai()
def info(c):
    query = db.unihan.lookup_char(c)
    glyph = query.first()
    pp({k: getattr(glyph,k) for k in glyph.__dict__ if k.startswith('k')})

def defn(c):
    query = db.unihan.lookup_char(c)
    glyph = query.first()
    return c, glyph.kDefinition

def lu(s):
    query = db.unihan.reverse_char(s)
    return ''.join([g.char for g in query])

def lookup(s):
    query = db.unihan.reverse_char(s)
    print('\n'.join([f'{g.char} {g.kMandarin} - {g.kDefinition}' for g in query]))

# >>> from auto import *
# >>> from chinese import *
# >>> defn('囗')
# ('囗', 'erect, proud; upright; bald')
# >>> lu('good')
# '㑘㑤㓛㘬㙉㚃㚒㚥㛦㜴㜺㝖㤛㦝㫑㭋㰬㱅㱡㳤㹏㹛㽥㾎㿲䃽䄈䄉䄐䄙䋬䌖䌝䌤䌧䌳䏂䐌䐚䑞䒁䒏䒐䙤䚱䚷䚸䜴䝕䝨䢇䣨䣩䤒䩂䩇䩊䫑䫢䮐䯭䱼䴆佳佼功吉咊善塡填好姤姽娥宓昌淑祉祥祦祯祺禎福禔禨羑羭腆臧良貨賍賢贒贓贜贤货赃邲醇頔顓颛餱良祥𠿭'

# >>> lu('ashamed')
# '㗤㗳㘂㤰㥏㥴㥾㦦㦬䀣䎵䚼䣯䩄䩅䩆䩋䪾僯嘁媿忝忸怍怩恥惭愧慙慚懅瞢羞耻覥觍'
# >>> 

# >>> lookup('sin')
# 㐰 xìn - (ancient form of 信) to believe in; to trust, truth, sincerity, confidence, a pledge or token
# 㑟 běng - insincere and cunning person; a pretentious person
# 㒤 chè - to have one's heart won; to submit, admire, etc. sincerely and willingly, (interchangeable 懾) to fear; to dread; to be scared of
# 㒨 None - (ancient form of 仙) an immortal; a fairy; a genie
# 㓣 qià - to sink into; to pierce, (ancient form of 割) to cut; to hack; to reap
# 㕇 lā - rocks collapsing (descriptive of sound), big pieces of rocks
# 㕩 pàng - (non-classical form) sound of tapping; sound of striking, opposing voices
# 㕷 huà - (corrupted form 咟) to call, to yell, anxious, dazed, image sound, an exclamation expressing sound (such as clap hands; to fire a gun; to strike; sound of firecracker etc.)
# 㖡 yè - the birds singing during the night; (Cant.) interjection to indicate the speaker is thinking
# 㖪 huò - sound of surprising, to laugh loudly, to flow off, loquacious, sound; voice; tone
# 㖷 shí - bird singing, (same as 啼) to cry; to mourn; to howl, to twitter; to crow
# 㗢 hóng - loquacious, the sound of singing, to sing in a loud voice, loud
# 㙚 xīng - red colored hard and solid mud (soil; clay; earth)
# 㙩 liáo - an enclosing wall
# 㚉 gǔ - (corrupted form) to make a profit on sell and buy; the profit in business, (interchangeable 嬴) a overplus; gain; profit; abundance
# 㚒 shǎn - concealed the stolen goods in one's dress
# 㛁 pēng - quick; urgent; anxious, loyal sincere and respectful
# 㛍 qiè - to have one's ambition fulfilled; to be successful in one's career; (same as 愜) pleasing; satisfying; to gratify or be gratified, undignified; improper
# 㜪 shēn - (same as 嫀) name of a family or a clan, name of country (in ancient times)
# 㜸 niè - (non-classical form of 孽) sin; evil; retribution, the son of a concubine
# 㝄 chún - (ancient form of 純) pure, sincere; honest; faithful
# 㝭 xǐng - (non-classical form) to awake (from errors, illusions, etc. to come to one's sense, (interchangeable 惺) clever; wise, wavering; indecisive
# 㞟 diàn - savings and (or) reserves; (same as U+5960 奠) to settle; to lay; (same as U+588A 墊) to advance (money), to cushion, to sink into; (said of manner) dignified; stately; graceful
# 㞼 chéng - (same as 丞) to respectfully receive, to flatter; to pay court to
# 㡝 fèng - a napkin, kerchief, a headgear; articles for dressing the hair, a calligrapher's or painter's signature, seal, dedicatory notes, etc. on a painting, etc.
# 㢒 chá - an almost collapsing house
# 㢲 xùn - (same as 巽) the 5th of the Eight Diagrams 八卦, South-east, Mild, bland, insinuating, peaceful words
# 㣒 cèng - hair-raising, hairiness
# 㤌 gān - (same as 甘) to have one's heart own; to submit, admire, etc. sincerely and willingly
# 㤣 None - (same as 恲) noble; disinterested; generous; energetic; liberal, to divulge; to leak out, to feel dull and listless or depressed
# 㤩 kè - (same as 恪) to respect; to venerate, grave and stern; of ornament -- splendid, imposing
# 㥦 qiè - (a variant of 愜) satisfied; contented; cheerful, appropriate; fitting; apposite, to have one's heart won; to summit; admire, etc. sincerely and willingly
# 㥫 None - (a variant of 惇) honest; sincere; kind; generous
# 㦄 má - hard to say or predict, difficult to speak out (for fear of embarrassing or paining others, etc.) not easy to express with words
# 㦚 biǎn - melancholy; grievous; mournful, urgent; pressing
# 㦨 lán - (same as 嬾) lazy; indolent; idle; inactive; reluctant; disinclined
# 㦲 None - (non-classical form of 哉) a particle expressing surprise, admiration, or grief, an expletive
# 㧥 xiǎn - to nip with the fingers; to take a pinch; to take up as with tongs
# 㧭 qióng - to get something with both raising hands
# 㧯 lǎo - a bucket made of willow, (a dialect) to lift (especially when only a single person is involved)
# 㪅 None - (same as 更) to change, to alter
# 㪇 xiàn - to disseminate; to spread, the weak sound of a Chinese musical instrument with seven or five strings
# 㪟 None - (same as 敦) to regard as important, to esteem, honest; sincere; generous
# 㪨 shàn - to mend; to repair; to copy; to write out
# 㬮 nàn - gentle; mild; temperate, tender; loving; caressing
# 㬱 tì - (same as 替) to replace; to substitute; to decay; to decline, (a variant 朁) if, supposing, nevertheless
# 㬵 xiáo - the shinbone, or tibia, (same as 交) to intersect, the sun and the moon in the sky, (simpfied form 膠) glue; gum, resin; sap, anything sticky
# 㭈 jué - a basin; a bowl
# 㭌 móu - (same as 桙) a basin; a bathtub, a kind of tool or utensil, (interchangeable 模) form or shape of a thing; style; pattern; appearance; look, a sample
# 㭏 wěi - (simplified form of 椲) a kind of wood (used as a kind of material to make basin and bowl, etc.); (same as 楎) a peg for hanging things on, a clothes-horse
# 㭠 xiǎn - None
# 㮐 shěng - a rack or a stand with three sticks to cross each other, a chopping board
# 㮒 yān - wood, (same as 禋) to worship with sincerity and reverence, to offer sacrifices to the Heaven
# 㮱 shēn - (said of grass, trees, vegetation and flora), (non-classical form of 森) luxuriant; exuberant; lush; flourishing
# 㮼 None - None
# 㯸 jǐn - a basin
# 㱁 shì - to ask; to inquire; to investigate, (same as 款) sincerity; article, item, etc., to entertain, slowly
# 㱠 kū - withered; dry, calamity; disaster, (ancient form 辜) sin; crime; guilt
# 㱡 shēng - the soul out of one's body; as good as dead
# 㱫 làn - destroyed or ruined; to rot or decay; to disintegrate or decompose
# 㲔 xiān - woolen textiles; fine cloth
# 㴘 mào - to ooze out; to well out; to spring out, to well up; flood tide; the water is rising
# 㴴 chén - (ancient form of 湛) (interchangeable 沈 沉) sink, deep; profound, joy; delight, happy; peaceful (interchangeable 潭) deep water; deep pool, leisurely; relaxed, dewy, full; filled, wet; damp; moist, clear (interchangeable 浸) to dip; to immerse; to soak, swellings; roaring waves and billows, flowing water, (same as 霪 淫) to rain cats and dogs for a long time, a river in ancient times in Henan province Jiyuanxian (blocked)
# 㴾 bó - (same as 渤) (of water) swelling or rising; an inland sea among today's Liaoning, Hebei and Shandong Provinces
# 㵴 cáng - to sink
# 㶍 xiǎn - name of a stream
# 㶓 cáng - to sink; to drown; to be submerged
# 㷀 qióng - (same as 焭,煢,惸) solitary; alone; single; brotherless; friendless; helpless, dice; a kind of gambling game played in ancient times
# 㷈 è - embers kept for starting a new fire, or any burning object (covered by ashes) which causes a fire disaster, the farm products getting heated with piling up and closing completely
# 㷣 xīng - red; the color of fire
# 㷻 wú - (same as 無) without, none, a negative (a variant 嬭) to burn food in cocking; singed; burnt
# 㷽 None - None
# 㼚 gāng - earthware; pottery (a basin; a pot; a bowl. a cistern; a crock), (interchangeable 缸) a big earthen jar
# 㼜 àng - (same as 盎) a basin; pot; bowl or dish, sleek; well-favoured, abundant, a musical instrument
# 㼝 fàn - (same as 盌) (a variant of 碗) a bowl; a basin; a cup; a dish
# 㼤 qiè - earthenware (a basin; a pot; a bowl; a crock with a narrow opening)
# 㼩 chéng - concave channels of tiling, a long-necked jar, utensil; instrument; implement
# 㼬 xìng - earthenware (a basin; a pot; a bowl; a crock etc.)
# 㼳 shěng - earthenware (a basin; a pot; a bowl; a crock etc.)
# 㼴 ǒu - an earthen vessel; a basin; a pot; a jar
# 㼵 dì - a small basin; a bowl. a cup; a pot; a jar
# 㼶 yú - earthenware (a basin; a pot; a bowl; a crock etc.)
# 㼷 chuán - a basin, (same as 甎) a brick; a square tile
# 㼸 róng - earthenware (a basin; a pot; a bowl; a crock etc.)
# 㽀 zhèng - earthenware (a basin; a pot; a bowl; a crock etc.)
# 㽉 xiàn - a big jar; a big basin
# 㽝 lì - to sink; to fall, to entrap, to crush; to capture
# 㽮 None - (same as 星) a point of light, stars; planets, a spark
# 㾌 xuǎn - (same as 癬) ringworm, used for various diseases of the skin
# 㾾 xiān - disease of the throat, something stuck in the throat, to be stung, emaciated; illness of losing flesh
# 㿅 xiǎn - (same as 癬) ringworm, used for various diseases of the skin
# 㿽 xī - a small bowl; a small basin
# 䀁 yòu - a small bowl; a small basin, a kind of vessel to remove (or to strain out) the water
# 䀂 ān - a big basin
# 䀉 qiáo - food containers (bowl; basin, etc.) used in ancient times
# 䁝 yíng - deluding and causing disorder (interchangeable 熒) lights shining; sparkling; twinkling; shimmering
# 䃍 zhào - (ancient form of 墜) to fall down; to sink
# 䃏 xīng - a kind of rock
# 䃽 guǐ - name of a mountain (of warship), (same as 禔) happiness; good fortune; good luck; blessing, (same as standard form 祓) to exorcise; to remove evil; to cleanse; to clean; to wash away
# 䄄 yīn - achievement; accomplishment, (non-classical form of 禋) to worship with sincerity and reverence, to offer sacrifices to the Heaven
# 䄐 quàn - to worship; to honor by a service or rite; to offer sacrifices, happiness; good fortune; good luck; blessing; bliss
# 䄙 míng - happiness; good luck; good fortune; blessing; bliss
# 䄠 shàn - (ancient form of 禪) to sacrifice to heaven, the imperial power, as only the emperor was allowed to offer these sacrifices, to cleanse; to exorcize, of Buddhism; Buddhist
# 䄤 lài - to sink; to fall; decadent, to idle about; to be negligent of worship
# 䄳 xiān - None
# 䄽 tiǎn - (same as U+79C8 秈, U+7C7C 籼) common rice, as distinguished from glutinous rice; (corrupted form of U+413C 䄼) name of a place in ancient times
# 䅁 àn - to husk rice; to get the grains by oppressing the ears of the rice plant
# 䆄 zhǎn - a bundle, a bundle of rice plant
# 䆗 yǎo - deep and dark; profound, (same as 窈) tranquil; placid; serene, soft and pleasing; plausible; exquisite; very pleasant
# 䇂 qiān - (ancient form) fault; sin
# 䈥 jīn - (non-classical form of 筋) tendons; sinews; muscles, name of a variety of bamboo
# 䉌 suì - crude bamboo mats, a vessel for raising silk-worms
# 䉳 xiān - name of a variety of bamboo, a domicile; record of the population
# 䋌 jiǎng - (ancient form 堅) strong; durable; solid; firm; stable, (same as 䋗) tight; firm, pressing
# 䋗 None - (same as 䋌) (same as 堅) strong and durable, solid and firm; tight; pressing
# 䋮 jìn - (the large seal; a type of Chinese calligraphy) (same as 紟) a sash, to tie, a kind of cloth or textiles, lapel of a Chinese dress, a single coverlet
# 䋲 chě - (non-classical form of U+7E69 繩) a rope; a cord, to restrain, to rectify; to correct
# 䌞 liǎn - a knot to hang the apparatus made of reed for raising silkworms, a rope
# 䏚 chǎo - small, missing; wanting; lost, the floating ribs on the sides of the trunk
# 䏝 zhuān - (simplified form of 膞) sincere; earnest, a part of offering in sacrifice, gizzard of a fowl, chopped meat, small pig, the kneecap; patella, bone of one's limbs
# 䏪 èr - tendon (of meat animals); sinews; muscles
# 䐔 bǐn - muscle of the calf (of the leg), tendon (of meat animals), stopping and rising of the pulse like a plaited ropes
# 䑶 qiàn - sprightly boat; light boat
# 䒓 kǎi - to do violence, perverse; rebellious, calamities; tribulations; miseries; crime; sin
# 䒼 qū - (same as 曲) a bamboo tray for raising silkworms
# 䓧 cì - (same as 亟) urgent; pressing
# 䓰 yīn - absinthin, Artemisia capillaris, a kind of medicinal herb
# 䖍 qián - (same as 虔) to act with reverence, devout; sincere
# 䖨 shí - mantis, (same as 蟅) ground beetle (Eupolyphage sinensis)
# 䗌 xīng - dragonfly
# 䘪 chōng - clothes without hem; ragged garments; a garment without a lining, single
# 䘳 jīn - (interchangeable 襟) a garment of single thickness, lapel of a garment, collar of a robe formerly worn by the literati, therefore used for educated classes
# 䘵 lù - hissing sound of the clothes
# 䙒 xù - to store or save up; to hoard, to strip off; to deprive of, to undress forcibly
# 䙴 None - to soar as a bird, (ancient form of U+9077 遷) to move, to change
# 䚇 shěng - to observe; to inspect carefully, leaking out, a measurement, (non-classical of 省) economical, a province, to save; to avoid
# 䚯 tǎo - (ancient form of 討) to quell (uprising, rebellion, etc.) to punish (another nation, etc.) by force fo arms, sound; voice; tone
# 䚷 yī - to treat; to detain, according to one's wishes, good words; honest; sincere words, an echo, joke; witticism; pleasantry; jest; fun
# 䚻 yáo - (ancient form of 謠) to sing, a ballad, rumour; slander; a false report, from, to follow, to undertake; to attend to
# 䝧 mín - capital (in business), to compute taxes
# 䝾 fù - to bestow; to give, natural endowment or gifts, tax; revenue, to spread; to diffuse, to compose or sing, one of the Chinese literary forms akin to poetry
# 䞉 shèng - (same as 賸) a surplus; an overplus, remains, superfluous
# 䠾 shǎn - to dodge; to ward off
# 䡪 shàn - fan of a carriage
# 䢭 yàn - to cover; to screen; to shade; to conceal; to shut off, to block, to shift; to move, to forward; to convey, to walk
# 䣧 yì - (interchangeable 黓) black, color of the wine, sweet; honeyed; or pleasing
# 䤛 qiú - component parts of a cross-bow, (same as 銶) a single headed hatchet
# 䤶 yè - a hammer; a mallet; a bludgeon, agricultural tools; farming implements, an iron (for pressing clothes)
# 䤼 xiàn - metal wire
# 䥇 shàn - chemical element; Sarmarium (Sm); old translation of (鋱) Tb, (same as 釤) a sickle with a long handle, to swing a sickle to cut (grass or wheat)
# 䥈 mǔ - the symbol for Cobalt, an iron (for pressing clothes)
# 䥱 xiě - to melt or cast (metal) by using a mould, (non-classical form of 寫) to write; to draw
# 䥾 xiě - (simplified form of U+4971 䥱) to melt or cast (metal) by using a mold; (non-classical form of U+5BEB 寫) to write; to draw
# 䦂 shàn - (simplified form of U+4947 䥇) sarmarium (Sm); old ideograph for U+92F1 鋱, terbium (Tb); (same as U+91E4 釤) a sickle with a long handle, to swing a sickle to cut (grass or wheat)
# 䦅 shàn - (simplified form of 鐥) a kind of weapon used in ancient times, (same as 釤) a sickle with a long handle, to swing a sickle to cut (grass or wheat)
# 䦈 jiē - (ancient form of 嗟) to sigh in lamentation; to lament; an exclamation expressing grief or regret; to exclaim, name of a hill
# 䦕 pēng - (same as 閛) bang of the door; the sound of opening or closing the door
# 䧕 chéng - (same as 域) boundary; a frontier, a region; a country, (ancient form of 城) a city; a town
# 䧗 bì - mountains collapsing; a land-slide
# 䨘 xiàn - (same as U+9730 霰) sleet
# 䨢 dàn - (same as 霮) a passing cloud; floating clouds, densely covered by clouds; gathering clouds
# 䨷 xiàn - (same as 霰) sleet
# 䩱 shù - a scabbard; a sheath, remaining; overplus; surplus, sin; evil, the front of a cutting strip of cloth
# 䪡 None - (same as 齏) to fall down; to sink
# 䪩 yín - (same as 吟) to chant; to intone; to sing; to recite; to moan; to sigh
# 䪬 bó - sound of pressing something down
# 䪳 yǔn - slanted face causing by the paralyzed of the facial nerve
# 䫆 chéng - the front and back of the neck
# 䫢 sī - good; fine; excellent, pleasing, a wry neck
# 䫪 shuǎng - ugly; repulsive
# 䮪 chéng - (corrupted form) (same as 騬) to geld a horse or ass, etc.
# 䰧 hū - sinister, evil and shrewd
# 䱆 shéng - (same as 鱦) small fish, spawn, or roe, frog group
# 䱇 shàn - (same as 鱔) the eel
# 䱉 shàn - (corrupted form of 䱇) (same as 鱓,鱔) an eel
# 䲺 gàn - birds singing; chirps
# 䳙 xǐng - a egret-like bird, a kind of water bird
# 䳚 kàn - a sort of nightingale which is said to sing for the dawn; also the name for a large bat with awing-spread of two feet, a sort of pheasant
# 䴪 lù - a fabulous creature, something like a deer, with a single horn
# 䶛 là - to separate the meat from the bones with teeth, the sound of using teeth to separate the meat from the bones
# 业 yè - profession, business; GB radical 111
# 丞 chéng - assist, aid, rescue
# 个 gè - numerary adjunct, piece; single
# 乘 chéng - ride, ascend; avail oneself of; numerary adjunct for vehicles
# 亊 shì - affair, matter, business; to serve; accident, incident
# 事 shì - affair, matter, business; to serve; accident, incident
# 亨 hēng - smoothly, progressing, no trouble
# 亶 dǎn - sincere; real, true; truth
# 从 cóng - from, by, since, whence, through
# 仙 xiān - Taoist super-being, transcendent, immortal
# 伩 xìn - trust, believe; letter; (Cant.) small
# 伸 shēn - extend, stretch out, open up; trust
# 伽 jiā - transcription of sanskrit 'gha' in buddhist texts ('samgha', etc.); (nursing; attending; entertainer) (Jap.); tample; in Chinese this character is not used alone
# 侁 shēn - crowd
# 信 xìn - trust, believe; letter
# 俳 pái - actor; vaudeville show; insincere
# 個 gè - numerary adjunct, piece; single
# 倘 tǎng - if, supposing, in event of
# 倥 kōng - boorish, ignorant; urgent, pressing
# 倩 qiàn - beautiful, lovely; son-in-law
# 傥 tǎng - if, supposing, in case
# 僊 xiān - Taoist super-being, transcendent, immortal
# 僐 shàn - None
# 僤 dàn - sincere
# 僿 sài - small, minute; lacking sincerity
# 儃 chán - None
# 儻 tǎng - if, supposing, in case
# 先 xiān - first, former, previous
# 兟 shēn - to advance
# 冼 xiǎn - a surname
# 剩 shèng - leftovers, residue, remains
# 务 wù - affairs, business; must, should
# 勑 chì - reward; sincere
# 務 wù - affairs, business; must, should
# 勝 shèng - victory; excel, be better than
# 匜 yí - basin; container for wine
# 卂 xùn - to fly rapidly
# 升 shēng - arise, go up; hoist; advance
# 单 dān - single, individual, only; lone
# 単 dān - same as 單 U+55AE, single, individual, only; lone
# 吟 yín - sing, hum; recite; type of poetry
# 吱 zhī - chirping, squeaking, hissing
# 吲 yǐn - smile at; sneer at
# 呏 shēng - gallon; quart
# 呭 yì - final particle expressing consent; talkative
# 呻 shēn - groan, moan; recite with intonation
# 咏 yǒng - sing song or poem, hum, chant
# 咣 guāng - the sound of large door closing
# 哂 shěn - smile, laugh at, sneer at; (Cant.) a final particle indicating doing something to the full extent possible
# 哼 hēng - hum; sing softly; groan, moan; (Cant.) an interjecting indicating disapproval
# 唱 chàng - sing, chant, call; ditty, song
# 商 shāng - commerce, business, trade
# 啝 hé - (Cant.) final partical expressing surprise
# 啭 zhuàn - sing, chirp, warble, twitter
# 善 shàn - good, virtuous, charitable, kind
# 喎 wāi - a wry mouth; (Cant.) a final particle expressing contradiction, quotation, etc.
# 單 dān - single, individual, only; lone
# 噺 xīn - story, talk
# 囀 zhuàn - sing, chirp, warble, twitter
# 囟 xìn - top of the head; skull
# 圣 shèng - holy, sacred
# 坠 zhuì - fall down, drop, sink, go to ruin
# 城 chéng - castle; city, town; municipality
# 堕 duò - fall, sink, let fall; degenerate
# 堘 chéng - a raised path between field which acts as a dyke
# 塍 chéng - a raised path between fields, a dike
# 墜 zhuì - fall down, drop, sink, go to ruin
# 墠 shàn - smooth, hard spot made level for sacrificial altar
# 墡 shàn - chalk
# 墬 dì - to fall, sink
# 墮 duò - fall, sink, let fall; degenerate
# 声 shēng - sound, voice, noise; tone; music
# 売 mài - sell; [NOT casing, shell, husk]
# 壳 ké - casing, shell, husk
# 如 rú - if, supposing; as if; like, as
# 姓 xìng - one's family name; clan, people
# 姺 shēn - name of an ancient state
# 娍 chéng - None
# 娠 shēn - pregnant
# 婵 chán - beautiful, lovely, pretty, graceful
# 嬗 shàn - succession to the throne
# 孼 niè - misfortune; sin, evil
# 宂 rǒng - scattered, mixed affairs; duties; occupation business
# 实 shí - real, true; honest, sincere
# 実 shí - real, true; honest, sincere
# 宬 chéng - archives; surname
# 宸 chén - imperial; imperial palace
# 尟 xiǎn - surname; fresh
# 尠 xiǎn - very few; seldom, rarely
# 崦 yān - a mountain in Kansu, where there is a cave into which the sun is said to sink at night
# 嵊 shèng - district in Shaohsing, Chekiang
# 庖 páo - kitchen; cooking, cuisine
# 廯 xiān - None
# 彊 jiàng - stubborn, uncompromising
# 従 cóng - from, by, since, whence, through
# 從 cóng - from, by, since, whence, through
# 忏 chàn - regret, repent; confess sins
# 忱 chén - truth, sincerity; sincere
# 急 jí - quick, quickly; urgent, pressing
# 性 xìng - nature, character, sex
# 恂 xún - careful, sincere, honest; trust
# 恳 kěn - sincere, earnest, cordial
# 悃 kǔn - sincere, genuine, honest, loyal
# 悫 què - sincerity, honesty; modest
# 惇 dūn - be kind, cordial, sincere
# 惓 quán - careful, sincere, candid
# 惺 xīng - intelligent, clever, astute
# 愊 bì - sincere, honest; depressed
# 愨 què - sincerity, honesty; cautious
# 愫 sù - guileless, sincere, honest
# 愼 shèn - act with care, be cautious
# 愿 yuàn - sincere, honest, virtuous
# 慤 què - sincerity, honesty; modest
# 慥 zào - sincere, earnest
# 懇 kěn - sincere, earnest, cordial
# 懴 chàn - regret, repent; confess sins
# 懺 chàn - regret, repent; confess sins
# 成 chéng - completed, finished, fixed
# 戩 jiǎn - exterminate, destroy; blessing
# 戬 jiǎn - exterminate, destroy; blessing
# 扇 shàn - fan; door panel
# 承 chéng - inherit, receive; succeed
# 挚 zhì - sincere, warm, cordial; surname
# 掸 dǎn - to dust; a duster
# 搧 shān - fan; strike on face; stir up
# 摯 zhì - sincere, warm, cordial; surname
# 撣 dǎn - to dust; a duster
# 擅 shàn - monopolize; claim; arbitrarily; to dare
# 敦 dūn - esteem; honest, candid, sincere
# 新 xīn - new, recent, fresh, modern
# 旌 jīng - banner or flag adorned with feathers; to signal
# 既 jì - already; de facto; since; then
# 旣 jì - already; de facto; since; then
# 旭 xù - rising sun; brilliance; radiant
# 旸 yáng - rising sun; sunshine
# 昇 shēng - rise, ascent; peaceful; peace
# 星 xīng - a star, planet; any point of light
# 晟 chéng - clear, bright; splendor, brightness
# 晠 shèng - None
# 晨 chén - early morning, daybreak
# 暘 yáng - rising sun; sunshine
# 暵 hàn - dry by exposing sun
# 曙 shǔ - bright, light of rising sun
# 朁 cǎn - if, supposing, nevertheless
# 朣 tóng - the rising moon
# 朴 pǔ - simple, unadorned; sincere; surname; a tree
# 杻 chǒu - ligustrum sinenese, tree
# 椉 chéng - None
# 業 yè - profession, business, trade
# 樿 shàn - coffin
# 歌 gē - song, lyrics; sing, chant; praise
# 殻 qiào - casing, shell, husk, hull, skin
# 殼 ké - casing, shell, husk, hull, skin
# 毨 xiǎn - None
# 氙 xiān - xenon
# 氥 xī - xenon
# 氼 nì - to sink; to drown to be given over to
# 汛 xùn - high water, flood tides
# 汨 mì - Mi(luo) river in Hunan province where Qu Yuan drowned himself; to sink; used (erroneously) for U+6C69 汩
# 沈 chén - sink, submerge; addicted to; surname
# 沉 chén - sink, submerge; addicted to
# 沒 méi - not, have not, none; to drown, sink
# 没 méi - not, have not, none; drown, sink
# 沦 lún - be lost; sink, be submerged
# 洆 chéng - None
# 洒 sǎ - sprinkle; scatter; pour; to wipe away; to shiver
# 津 jīn - ferry; saliva; ford
# 淪 lún - be lost; sink, be submerged
# 渑 miǎn - name of a river in Shandong
# 渰 yǎn - (of cloud) forming or rising
# 渻 shěng - None
# 湮 yān - bury, sink, block up; stain
# 滃 wēng - swelling, rising, dispersing
# 滎 xíng - county in Henan; rising and dashing of waves
# 澠 miǎn - name of a river in Shandong
# 澶 chán - still water, placid, tranquil
# 瀋 shěn - juice; liquid; water; leak, pour
# 焄 xūn - rising flames or fumes; aroma
# 煋 xīng - None
# 煽 shān - stir up, incite, agitate, provoke
# 燂 tán - smoke, fumes; tobacco, opium; (Cant.) to singe
# 燘 měi - (Cant.) to suck or chew without using the teeth
# 燹 xiǎn - fire; wild fires
# 燼 jìn - cinders, ashes, embers; remnants
# 牲 shēng - sacrificial animal; animal
# 狌 shēng - None
# 狝 xiǎn - hunt; autumn hunting; to capture with a fine net
# 独 dú - alone, single, solitary, only
# 猩 xīng - species of orangutan
# 獨 dú - alone, single, solitary, only
# 獮 xiǎn - hunt; autumn hunting; to capture with a fine net
# 珹 chéng - type of jade; pearl
# 琞 shèng - None
# 瑆 xīng - None
# 生 shēng - life, living, lifetime; birth
# 申 shēn - to state to a superior, report; extend; 9th terrestrial branch
# 癣 xuǎn - ringworms
# 癬 xuǎn - ringworms
# 盂 yú - basin; cup
# 盆 pén - basin, tub, pot, bowl
# 盌 wǎn - bowl, basin, cup
# 盔 kuī - helmet; bowl; basin
# 盛 shèng - abundant, flourishing; contain; fill
# 省 shěng - province; save, economize
# 睲 xǐng - None
# 矧 shěn - much more, still more; the gums
# 硟 chàn - (Cant.) to slip; to work and polish gems
# 磰 shàn - None
# 礽 réng - blessings, happiness
# 祉 zhǐ - happiness, blessings, good luck
# 祚 zuò - throne; bless; blessing, happiness
# 祜 hù - blessing, happiness, prosperity
# 祝 zhù - pray for happiness or blessings
# 神 shén - spirit, god, supernatural being
# 祦 wú - happiness; good fortune good luck; blessing; bliss
# 祲 jìn - ominous or sinister spirit; vigor
# 祿 lù - blessing, happiness, prosperity
# 禄 lù - blessing, happiness, prosperity
# 禅 chán - meditation, contemplation (DKW: 24787')
# 福 fú - happiness, good fortune, blessing
# 禛 zhēn - to receive blessings in a sincere spirit
# 禪 chán - meditation, contemplation (dhyana); to level ground for altar; abdicate
# 秈 xiān - non-glutinous long grain rice
# 穨 tuí - ruined, decayed; to disintegrate
# 竏 qiān - kiloliter
# 竓 háo - milliliter
# 笃 dǔ - deep, true, sincere, genuine
# 筅 xiǎn - bamboo brush; halberd
# 筬 chéng - reed of a loom
# 箇 gè - numerary adjunct, piece; single
# 箲 xiǎn - None
# 箵 xīng - None
# 篤 dǔ - deep, true, sincere, genuine
# 籼 xiān - non-glutinous long grain rice
# 紳 shēn - girdle; tie, bind; gentry
# 綪 qiàn - dark red
# 綫 xiàn - line, thread, wire; clue
# 線 xiàn - thread, line, wire; clue
# 繕 shàn - repair, mend; rewrite, transcribe
# 繩 shéng - rope, string, cord; measure, restrain
# 线 xiàn - line, thread, wire; clue
# 绳 shéng - rope, string, cord; control
# 缮 shàn - repair, mend; rewrite, transcribe
# 缽 bō - earthenware basin; alms bowl
# 罪 zuì - crime, sin, vice; evil; hardship
# 美 měi - beautiful, pretty; pleasing
# 羡 xiàn - envy, admire; praise; covet
# 羨 xiàn - envy, admire; praise; covet
# 聖 shèng - holy, sacred; sage
# 聲 shēng - sound, voice, noise; tone; music
# 肫 zhūn - the gizzard of a fowl; honest, sincere
# 胜 shèng - victory; excel, be better than
# 胶 jiāo - glue, gum, resin, rubber; sound; shin bone
# 脤 shèn - raw meat for sacrifice
# 腎 shèn - kidneys; testes, gizzard
# 腥 xīng - raw meat; rank, strong-smelling
# 腺 xiàn - gland
# 膠 jiāo - glue, gum, resin, rubber
# 膳 shàn - meals, provisions, board
# 臣 chén - minister, statesman, official
# 艰 jiān - difficult, hard; distressing
# 艱 jiān - difficult, hard; distressing
# 芒 máng - Miscanthus sinensis
# 若 ruò - if, supposing, assuming; similar
# 苮 xiān - None
# 茜 qiàn - madder, rubia cordifolia; reeds
# 荥 xíng - a county in Henan; the rising and dashing of waves
# 莘 shēn - long; numerous; a marsh plant whose root is used for medicine
# 蒨 qiàn - lush vegetation, luxuriant growth
# 蔳 qiàn - None
# 蕂 shèng - sesame
# 薪 xīn - fuel, firewood; salary
# 藎 jìn - a kind of weed; faithfulness
# 藓 xiǎn - moss, lichen
# 蘚 xiǎn - moss, lichen
# 蜃 shèn - marine monster which can change its shape; water spouts; clams
# 蝉 chán - cicada; continuous
# 蟬 chán - cicada; continuous
# 蟮 shàn - type of earthworm
# 蟺 shàn - earthworm
# 褟 tā - inner shirt or singlet
# 褼 xiān - None
# 親 qīn - relatives, parents; intimate
# 訊 xùn - inquire; ask; examine; reproach
# 訦 chén - sincere; faithful
# 設 shè - build; establish; display; particle of hypothesis, supposing
# 詠 yǒng - sing, hum, chant
# 誠 chéng - sincere, honest; true, real
# 誶 suì - speak ill of, vilify; berate; interrogate
# 諴 xián - in harmony; in agreement; sincere
# 諶 chén - sincere, faithful; surname
# 謆 shàn - beguile, cajole
# 謠 yáo - sing; folksong, ballad; rumor
# 謡 yáo - sing; folksong, ballad; rumor
# 謳 ōu - to sing; songs
# 讴 ōu - sing; songs
# 诚 chéng - sincere, honest; true, real
# 谌 chén - sincere, faithful; surname
# 谣 yáo - sing; folksong, ballad; rumor
# 賸 shèng - leftovers, residue, remains
# 贍 shàn - support, aid; to be sufficient; rich, elegant
# 贐 jìn - farewell present
# 趔 liè - not progressing; to be checked
# 跣 xiǎn - bare footed
# 跹 xiān - wander about, walk around; revolve
# 踧 cù - uneasiness, nervousness; level
# 蹮 xiān - to whirl, pirouette
# 躚 xiān - wander about, walk around; revolve
# 身 shēn - body; trunk, hull; rad. no. 158
# 輤 qiàn - a pall to cover the hearse
# 辛 xīn - bitter; toilsome, laborious; 8th heavenly stem
# 辠 zuì - crime, sin, vice; evil; hardship
# 辰 chén - early morning; 5th terrestrial branch
# 迅 xùn - quick, hasty, rapid, sudden
# 郕 chéng - state in Shandong province
# 鄩 xún - county in Shandong province
# 鄯 shàn - district in Gansu during the Tang dynasty
# 酢 cù - toast one's host with wine; to express juice by pressing
# 酰 xiān - acyl
# 醒 xǐng - wake up; sober up; startle
# 釤 shàn - samarium
# 鉢 bō - earthenware basin; alms bowl (Sanskrit paatra)
# 銑 xiǎn - mill
# 鋋 chán - None
# 鋗 xuān - a small basin; rings on a cart of carriage
# 鋮 chéng - person's name
# 鏾 sǎn - the trigger of a crossbow; crossbow
# 鐥 shàn - None
# 钵 bō - earthenware basin; alms bowl
# 铖 chéng - person's name
# 铣 xǐ - mill
# 镹 jiǔ - None
# 陞 shēng - promote, rise, ascend
# 陥 xiàn - submerge, sink, plunge; trap
# 陷 xiàn - submerge, sink, plunge; trap
# 隻 zhī - single, one of pair, lone
# 霋 qī - slight, passing
# 霎 shà - light rain, drizzle; an instant; passing
# 霰 sǎn - hail, sleet
# 頣 shěn - to view others with raised eyes
# 頹 tuí - ruined, decayed; disintegrate
# 顖 xìn - top of the head; skull
# 颓 tuí - ruined, decayed; disintegrate
# 饍 shàn - meals, provisions, board
# 駪 shēn - crowd
# 騂 xīng - red, brown, bay; neat, harmonious
# 騬 chéng - None
# 騸 shàn - geld, castrate
# 骍 xīng - red, brown, bay; neat, harmonious
# 骟 shàn - geld, castrate
# 髞 sào - high, imposing, eminent
# 鮏 xīng - None
# 鮮 xiān - fresh, new, delicious; rare, few
# 鯙 chún - Scomberomorus sinensis
# 鰆 chūn - Scomberomorus sinensis
# 鱓 shàn - eel
# 鱔 shàn - eel
# 鱻 xiān - fresh, new, delicious; rare, few
# 鲜 xiān - fresh; delicious; attractive
# 鳝 shàn - eel
# 黑 hēi - black; dark; evil, sinister
# 鼈 biē - a fresh-water turtle, Trionyx sinensis
# 鿬 tián - tennessine (element 117)
# 祿 None - blessing, happiness, prosperity
# 辰 None - early morning
# 沈 None - sink, submerge; addicted to; name
# 若 None - if, supposing, assuming; similar
# 杻 None - ligustrum sinenese, tree
# 淪 None - be lost; sink, be submerged
# 神 None - spirit
# 𠄘 None - None
# 𠉛 None - None
# 𠜎 xiàn - to castrate a fowl, a capon
# 𠱘 nì - (Cant.) contrary, opposing, against; disobedient
# 𠵈 None - (Cant.) to suck or chew without using the teeth
# 𠸺 nì - (Cant.) contrary, opposing
# 𡉼 None - None
# 𡟙 None - None
# 𡷫 None - None
# 𢱟 chǎn - to strike, flog
# 𣛮 None - None
# 𣲛 None - None
# 𣳈 None - None
# 𣺋 None - None
# 𥑥 chǎ - None
# 𥔱 shàn - (Cant.) to slip
# 𥖄 None - None
# 𥛶 None - None
# 𥪕 None - None
# 𦼦 None - None
# 𨃩 None - (Cant.) to slip, slide
# 𨛘 None - None
# 𨬢 None - None
# 𩦝 None - None
# 𬓼 tuí - ruined, decayed; to disintegrate
# >>> 
# >>> info('囗')
# {'kAccountingNumeric': None,
#  'kCangjie': 'BM',
#  'kCantonese': 'wai4',
#  'kCheungBauer': None,
#  'kCihaiT': '294.509',
#  'kCompatibilityVariant': None,
#  'kDefinition': 'erect, proud; upright; bald',
#  'kFenn': '765K',
#  'kFourCornerCode': '6000.0',
#  'kFrequency': None,
#  'kGradeLevel': None,
#  'kHDZRadBreak': '⼞[U+2F1E]:10710.080',
#  'kHKGlyph': None,
#  'kHangul': None,
#  'kHanyuPinlu': None,
#  'kHanyuPinyin': '10710.080:wéi,guó',
#  'kJapaneseKun': 'KAKOMU KUNI',
#  'kJapaneseOn': 'I KOKU',
#  'kKorean': 'KWUK WI',
#  'kMandarin': 'wéi',
#  'kOtherNumeric': None,
#  'kPhonetic': '1434',
#  'kPrimaryNumeric': None,
#  'kRSAdobe_Japan1_6': 'C+4459+31.3.0',
#  'kRSJapanese': None,
#  'kRSKanWa': None,
#  'kRSKangXi': '31.0',
#  'kRSKorean': None,
#  'kRSUnicode': '31.0',
#  'kSemanticVariant': None,
#  'kSimplifiedVariant': None,
#  'kSpecializedSemanticVariant': None,
#  'kTang': None,
#  'kTotalStrokes': '3',
#  'kTraditionalVariant': None,
#  'kVietnamese': None,
#  'kXHC1983': None,
#  'kZVariant': None}
# >>> dir(unicodedata)
# ['UCD', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'bidirectional', 'category', 'combining', 'decimal', 'decomposition', 'digit', 'east_asian_width', 'lookup', 'mirrored', 'name', 'normalize', 'numeric', 'ucd_3_2_0', 'ucnhash_CAPI', 'unidata_version']
# >>> help(auto.unicodedata.module())
# Help on built-in module unicodedata:
# 
# NAME
#     unicodedata
# 
# DESCRIPTION
#     This module provides access to the Unicode Character Database which
#     defines character properties for all Unicode characters. The data in
#     this database is based on the UnicodeData.txt file version
#     11.0.0 which is publicly available from ftp://ftp.unicode.org/.
#     
#     The module uses the same names and symbols as defined by the
#     UnicodeData File Format 11.0.0.
# 
# CLASSES
#     builtins.object
#         UCD
#     
#     class UCD(builtins.object)
#      |  Methods defined here:
#      |  
#      |  __getattribute__(self, name, /)
#      |      Return getattr(self, name).
#      |  
#      |  bidirectional(self, chr, /)
#      |      Returns the bidirectional class assigned to the character chr as string.
#      |      
#      |      If no such value is defined, an empty string is returned.
#      |  
#      |  category(self, chr, /)
#      |      Returns the general category assigned to the character chr as string.
#      |  
#      |  combining(self, chr, /)
#      |      Returns the canonical combining class assigned to the character chr as integer.
#      |      
#      |      Returns 0 if no combining class is defined.
#      |  
#      |  decimal(self, chr, default=None, /)
#      |      Converts a Unicode character into its equivalent decimal value.
#      |      
#      |      Returns the decimal value assigned to the character chr as integer.
#      |      If no such value is defined, default is returned, or, if not given,
#      |      ValueError is raised.
#      |  
#      |  decomposition(self, chr, /)
#      |      Returns the character decomposition mapping assigned to the character chr as string.
#      |      
#      |      An empty string is returned in case no such mapping is defined.
#      |  
#      |  digit(self, chr, default=None, /)
#      |      Converts a Unicode character into its equivalent digit value.
#      |      
#      |      Returns the digit value assigned to the character chr as integer.
#      |      If no such value is defined, default is returned, or, if not given,
#      |      ValueError is raised.
#      |  
#      |  east_asian_width(self, chr, /)
#      |      Returns the east asian width assigned to the character chr as string.
#      |  
#      |  lookup(self, name, /)
#      |      Look up character by name.
#      |      
#      |      If a character with the given name is found, return the
#      |      corresponding character.  If not found, KeyError is raised.
#      |  
#      |  mirrored(self, chr, /)
#      |      Returns the mirrored property assigned to the character chr as integer.
#      |      
#      |      Returns 1 if the character has been identified as a "mirrored"
#      |      character in bidirectional text, 0 otherwise.
#      |  
#      |  name(self, chr, default=None, /)
#      |      Returns the name assigned to the character chr as a string.
#      |      
#      |      If no name is defined, default is returned, or, if not given,
#      |      ValueError is raised.
#      |  
#      |  normalize(self, form, unistr, /)
#      |      Return the normal form 'form' for the Unicode string unistr.
#      |      
#      |      Valid values for form are 'NFC', 'NFKC', 'NFD', and 'NFKD'.
#      |  
#      |  numeric(self, chr, default=None, /)
#      |      Converts a Unicode character into its equivalent numeric value.
#      |      
#      |      Returns the numeric value assigned to the character chr as float.
#      |      If no such value is defined, default is returned, or, if not given,
#      |      ValueError is raised.
#      |  
#      |  ----------------------------------------------------------------------
#      |  Data descriptors defined here:
#      |  
#      |  unidata_version
# 
# FUNCTIONS
#     bidirectional(chr, /)
#         Returns the bidirectional class assigned to the character chr as string.
#         
#         If no such value is defined, an empty string is returned.
#     
#     category(chr, /)
#         Returns the general category assigned to the character chr as string.
#     
#     combining(chr, /)
#         Returns the canonical combining class assigned to the character chr as integer.
#         
#         Returns 0 if no combining class is defined.
#     
#     decimal(chr, default=None, /)
#         Converts a Unicode character into its equivalent decimal value.
#         
#         Returns the decimal value assigned to the character chr as integer.
#         If no such value is defined, default is returned, or, if not given,
#         ValueError is raised.
#     
#     decomposition(chr, /)
#         Returns the character decomposition mapping assigned to the character chr as string.
#         
#         An empty string is returned in case no such mapping is defined.
#     
#     digit(chr, default=None, /)
#         Converts a Unicode character into its equivalent digit value.
#         
#         Returns the digit value assigned to the character chr as integer.
#         If no such value is defined, default is returned, or, if not given,
#         ValueError is raised.
#     
#     east_asian_width(chr, /)
#         Returns the east asian width assigned to the character chr as string.
#     
#     lookup(name, /)
#         Look up character by name.
#         
#         If a character with the given name is found, return the
#         corresponding character.  If not found, KeyError is raised.
#     
#     mirrored(chr, /)
#         Returns the mirrored property assigned to the character chr as integer.
#         
#         Returns 1 if the character has been identified as a "mirrored"
#         character in bidirectional text, 0 otherwise.
#     
#     name(chr, default=None, /)
#         Returns the name assigned to the character chr as a string.
#         
#         If no name is defined, default is returned, or, if not given,
#         ValueError is raised.
#     
#     normalize(form, unistr, /)
#         Return the normal form 'form' for the Unicode string unistr.
#         
#         Valid values for form are 'NFC', 'NFKC', 'NFD', and 'NFKD'.
#     
#     numeric(chr, default=None, /)
#         Converts a Unicode character into its equivalent numeric value.
#         
#         Returns the numeric value assigned to the character chr as float.
#         If no such value is defined, default is returned, or, if not given,
#         ValueError is raised.
# 
# DATA
#     ucd_3_2_0 = <unicodedata.UCD object>
#     ucnhash_CAPI = <capsule object "unicodedata.ucnhash_CAPI">
#     unidata_version = '11.0.0'
# 
# FILE
#     (built-in)
# 
# 
# >>> help(unicodedata.east_asian_width)
# Help on built-in function east_asian_width in module unicodedata:
# 
# east_asian_width(chr, /)
#     Returns the east asian width assigned to the character chr as string.
# 
# >>> unicodedata.east_asian_width('a')
# 'Na'
# >>> 
# >>> unicodedata.east_asian_width('ִּּּ 造אּ'[2])
# 'N'
# >>> "aאִaa'[1]
#   File "<console>", line 1
#     "aאִaa'[1]
#              ^
# SyntaxError: EOL while scanning string literal
# >>> 
# >>> c=Cihai()
# >>> help(c)
# Help on Cihai in module cihai.core object:
# 
# class Cihai(builtins.object)
#  |  Cihai(config=None, unihan=True)
#  |  
#  |  Central application object.
#  |  
#  |  By default, this automatically adds the UNIHAN dataset.
#  |  
#  |  Attributes
#  |  ----------
#  |  config : dict
#  |  
#  |  Notes
#  |  -----
#  |  Inspired by the early pypa/warehouse applicaton object [1]_.
#  |  
#  |  **Configuration templates**
#  |  
#  |  The ``config`` :py:class:`dict` parameter supports a basic template system
#  |  for replacing :term:`XDG Base Directory` directory variables, tildes
#  |  and environmentas variables. This is done by passing the option dict
#  |  through :func:`cihai.config.expand_config` during initialization.
#  |  
#  |  Examples
#  |  --------
#  |  To use cihai programatically, invoke and install the UNIHAN [2]_ dataset:
#  |  
#  |  .. literalinclude:: ../examples/basic_usage.py
#  |      :language: python
#  |  
#  |  Above: :attr:`~cihai.data.unihan.bootstrap.is_bootstrapped` can check if the system
#  |  has the database installed.
#  |  
#  |  References
#  |  ----------
#  |  .. [1] UNICODE HAN DATABASE (UNIHAN) documentation.
#  |     https://www.unicode.org/reports/tr38/. Accessed March 31st, 2018.
#  |  .. [2] PyPA Warehouse on GitHub. https://github.com/pypa/warehouse.
#  |     Accessed sometime in 2013.
#  |  
#  |  Methods defined here:
#  |  
#  |  __init__(self, config=None, unihan=True)
#  |      Parameters
#  |      ----------
#  |      config : dict, optional
#  |      unihan : boolean, optional
#  |          Bootstrap the core UNIHAN dataset (recommended)
#  |  
#  |  add_dataset(self, _cls, namespace)
#  |  
#  |  bootstrap(self)
#  |  
#  |  ----------------------------------------------------------------------
#  |  Class methods defined here:
#  |  
#  |  from_file(config_path=None, *args, **kwargs) from builtins.type
#  |      Create a Cihai instance from a JSON or YAML config.
#  |      
#  |      Parameters
#  |      ----------
#  |      config_path : str, optional
#  |          path to custom config file
#  |      
#  |      Returns
#  |      -------
#  |      :class:`Cihai` :
#  |          application object
#  |  
#  |  ----------------------------------------------------------------------
#  |  Data descriptors defined here:
#  |  
#  |  __dict__
#  |      dictionary for instance variables (if defined)
#  |  
#  |  __weakref__
#  |      list of weak references to the object (if defined)
#  |  
#  |  ----------------------------------------------------------------------
#  |  Data and other attributes defined here:
#  |  
#  |  default_config = {'database': {'url': 'sqlite:////home/pi/.local/share...
# 
# >>> 
# >>> unihan=c.unihan
# >>> dir(unihan)
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'add_plugin', 'base', 'bootstrap', 'engine', 'is_bootstrapped', 'lookup_char', 'metadata', 'reverse_char', 'session', 'sql', 'with_fields']
# >>> 

# >>> query = unihan.lookup_char('好')
# >>> glyph = query.first()
# >>> glyph.kDefinition
# 'good, excellent, fine; well'
# >>> pp=pprint.pprint
# >>> pp({k: getattr(glyph,k) for k in glyph.__dict__ if k.startswith('k')})
# {'kAccountingNumeric': None,
#  'kCangjie': 'VND',
#  'kCantonese': 'hou2 hou3',
#  'kCheungBauer': None,
#  'kCihaiT': '378.103',
#  'kCompatibilityVariant': None,
#  'kDefinition': 'good, excellent, fine; well',
#  'kFenn': '552A',
#  'kFourCornerCode': '4744.7',
#  'kFrequency': '1',
#  'kGradeLevel': '1',
#  'kHDZRadBreak': None,
#  'kHKGlyph': '0871',
#  'kHangul': '호:0E',
#  'kHanyuPinlu': 'hǎo(6060) hāo(142) hào(115)',
#  'kHanyuPinyin': '21028.010:hǎo,hào',
#  'kJapaneseKun': 'KONOMU SUKU YOI',
#  'kJapaneseOn': 'KOU',
#  'kKorean': 'HO',
#  'kMandarin': 'hǎo',
#  'kOtherNumeric': None,
#  'kPhonetic': '481',
#  'kPrimaryNumeric': None,
#  'kRSAdobe_Japan1_6': 'C+1975+38.3.3 C+1975+39.3.3',
#  'kRSJapanese': None,
#  'kRSKanWa': None,
#  'kRSKangXi': '38.3',
#  'kRSKorean': None,
#  'kRSUnicode': '38.3',
#  'kSemanticVariant': None,
#  'kSimplifiedVariant': None,
#  'kSpecializedSemanticVariant': None,
#  'kTang': '*xɑ̀u *xɑ̌u',
#  'kTotalStrokes': '6',
#  'kTraditionalVariant': None,
#  'kVietnamese': 'háo',
#  'kXHC1983': '0445.030:hǎo 0448.030:hào',
#  'kZVariant': None}
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
## >>> unihan.bootstrap({})
## Total size: 6.7Mb
## 
## 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
