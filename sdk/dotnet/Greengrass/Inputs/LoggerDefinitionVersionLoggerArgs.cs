// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Greengrass.Inputs
{

    public sealed class LoggerDefinitionVersionLoggerArgs : global::Pulumi.ResourceArgs
    {
        [Input("component", required: true)]
        public Input<string> Component { get; set; } = null!;

        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        [Input("level", required: true)]
        public Input<string> Level { get; set; } = null!;

        [Input("space")]
        public Input<int>? Space { get; set; }

        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public LoggerDefinitionVersionLoggerArgs()
        {
        }
        public static new LoggerDefinitionVersionLoggerArgs Empty => new LoggerDefinitionVersionLoggerArgs();
    }
}
