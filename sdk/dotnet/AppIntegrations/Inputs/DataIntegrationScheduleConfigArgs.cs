// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppIntegrations.Inputs
{

    public sealed class DataIntegrationScheduleConfigArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The start date for objects to import in the first flow run. Epoch or ISO timestamp format is supported.
        /// </summary>
        [Input("firstExecutionFrom", required: true)]
        public Input<string> FirstExecutionFrom { get; set; } = null!;

        /// <summary>
        /// The name of the object to pull from the data source.
        /// </summary>
        [Input("object", required: true)]
        public Input<string> Object { get; set; } = null!;

        /// <summary>
        /// How often the data should be pulled from data source.
        /// </summary>
        [Input("scheduleExpression", required: true)]
        public Input<string> ScheduleExpression { get; set; } = null!;

        public DataIntegrationScheduleConfigArgs()
        {
        }
        public static new DataIntegrationScheduleConfigArgs Empty => new DataIntegrationScheduleConfigArgs();
    }
}
