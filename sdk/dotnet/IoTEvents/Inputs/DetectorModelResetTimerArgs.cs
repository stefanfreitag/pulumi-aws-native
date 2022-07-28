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
    /// Information required to reset the timer. The timer is reset to the previously evaluated result of the duration. The duration expression isn't reevaluated when you reset the timer.
    /// </summary>
    public sealed class DetectorModelResetTimerArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the timer to reset.
        /// </summary>
        [Input("timerName", required: true)]
        public Input<string> TimerName { get; set; } = null!;

        public DetectorModelResetTimerArgs()
        {
        }
        public static new DetectorModelResetTimerArgs Empty => new DetectorModelResetTimerArgs();
    }
}
