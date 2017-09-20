include("./jtalk.jl")
#tts = Jtalk.JTalk(voicePath="mei_normal")

tts = Jtalk.JTalk()
println("available voices:")
for item in Jtalk.getVoices(tts)
    println(item[:path])
end
Jtalk.setVoice(tts,rand(Jtalk.getVoices(tts)))
println("current voice: $(Jtalk.getVoice(tts)[:name])")
println("dic= $(Jtalk.getDic(tts))")

println("s  = $(Jtalk.getS(tts))")
println("p  = $(Jtalk.getP(tts))")
println("a  = $(Jtalk.getA(tts))")
println("b  = $(Jtalk.getB(tts))")
println("r  = $(Jtalk.getR(tts))")
println("fm = $(Jtalk.getFm(tts))")
println("u  = $(Jtalk.getU(tts))")
println("jm = $(Jtalk.getJm(tts))")
println("jf = $(Jtalk.getJf(tts))")
println("g  = $(Jtalk.getG(tts))")

Jtalk.speakAsync(tts,"聞こえますか")
Jtalk.waitUntilDone(tts)
