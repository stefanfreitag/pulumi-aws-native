// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Lex.Inputs
{

    /// <summary>
    /// Provides information for updating the user on the progress of fulfilling an intent.
    /// </summary>
    public sealed class BotFulfillmentUpdatesSpecificationArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Determines whether fulfillment updates are sent to the user. When this field is true, updates are sent.
        /// </summary>
        [Input("active", required: true)]
        public Input<bool> Active { get; set; } = null!;

        [Input("startResponse")]
        public Input<Inputs.BotFulfillmentStartResponseSpecificationArgs>? StartResponse { get; set; }

        /// <summary>
        /// The length of time that the fulfillment Lambda function should run before it times out.
        /// </summary>
        [Input("timeoutInSeconds")]
        public Input<int>? TimeoutInSeconds { get; set; }

        [Input("updateResponse")]
        public Input<Inputs.BotFulfillmentUpdateResponseSpecificationArgs>? UpdateResponse { get; set; }

        public BotFulfillmentUpdatesSpecificationArgs()
        {
        }
        public static new BotFulfillmentUpdatesSpecificationArgs Empty => new BotFulfillmentUpdatesSpecificationArgs();
    }
}
