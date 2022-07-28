// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Evidently.Inputs
{

    public sealed class LaunchMetricDefinitionObjectArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The JSON path to reference the entity id in the event.
        /// </summary>
        [Input("entityIdKey", required: true)]
        public Input<string> EntityIdKey { get; set; } = null!;

        /// <summary>
        /// Event patterns have the same structure as the events they match. Rules use event patterns to select events. An event pattern either matches an event or it doesn't.
        /// </summary>
        [Input("eventPattern", required: true)]
        public Input<string> EventPattern { get; set; } = null!;

        [Input("metricName", required: true)]
        public Input<string> MetricName { get; set; } = null!;

        [Input("unitLabel")]
        public Input<string>? UnitLabel { get; set; }

        /// <summary>
        /// The JSON path to reference the numerical metric value in the event.
        /// </summary>
        [Input("valueKey", required: true)]
        public Input<string> ValueKey { get; set; } = null!;

        public LaunchMetricDefinitionObjectArgs()
        {
        }
        public static new LaunchMetricDefinitionObjectArgs Empty => new LaunchMetricDefinitionObjectArgs();
    }
}
