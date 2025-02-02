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
    /// Defines the Amazon CloudWatch Logs destination log group for conversation text logs.
    /// </summary>
    public sealed class BotTextLogDestinationArgs : global::Pulumi.ResourceArgs
    {
        [Input("cloudWatch", required: true)]
        public Input<Inputs.BotCloudWatchLogGroupLogDestinationArgs> CloudWatch { get; set; } = null!;

        public BotTextLogDestinationArgs()
        {
        }
        public static new BotTextLogDestinationArgs Empty => new BotTextLogDestinationArgs();
    }
}
