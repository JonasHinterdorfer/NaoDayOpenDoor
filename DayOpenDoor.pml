<?xml version="1.0" encoding="UTF-8" ?>
<Package name="DayOpenDoor" format_version="5">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="behavior_1" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="ExampleDialog" src="behavior_1/ExampleDialog/ExampleDialog.dlg" />
    </Dialogs>
    <Resources>
        <File name="vacuum1" src="behavior_1/vacuum1.ogg" />
        <File name="heaven1" src="behavior_1/behavior_1/heaven1.ogg" />
        <File name="Elevator_Music_Kevin_MacLeod_-_Gaming_Background_Music_HD" src="Elevator_Music_Kevin_MacLeod_-_Gaming_Background_Music_HD.mp4" />
        <File name="output_audio" src="output_audio.mp3" />
        <File name="mouse-click-153941" src="mouse-click-153941.mp3" />
        <File name="output" src="output.mp3" />
        <File name="mikhael-landscape-paisaje" src="behavior_1/sounds/mikhael-landscape-paisaje.ogg" />
    </Resources>
    <Topics>
        <Topic name="ExampleDialog_enu" src="behavior_1/ExampleDialog/ExampleDialog_enu.top" topicName="ExampleDialog" language="en_US" nuance="enu" />
    </Topics>
    <IgnoredPaths />
    <Translations auto-fill="en_US">
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
    </Translations>
</Package>
