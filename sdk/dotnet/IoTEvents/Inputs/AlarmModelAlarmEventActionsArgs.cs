// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTEvents.Inputs
{

    /// <summary>
    /// Contains information about one or more alarm actions.
    /// </summary>
    public sealed class AlarmModelAlarmEventActionsArgs : global::Pulumi.ResourceArgs
    {
        [Input("alarmActions")]
        private InputList<Inputs.AlarmModelAlarmActionArgs>? _alarmActions;
        public InputList<Inputs.AlarmModelAlarmActionArgs> AlarmActions
        {
            get => _alarmActions ?? (_alarmActions = new InputList<Inputs.AlarmModelAlarmActionArgs>());
            set => _alarmActions = value;
        }

        public AlarmModelAlarmEventActionsArgs()
        {
        }
        public static new AlarmModelAlarmEventActionsArgs Empty => new AlarmModelAlarmEventActionsArgs();
    }
}
