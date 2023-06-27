// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CloudFormation.Inputs
{

    public sealed class ResourceVersionLoggingConfigArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Amazon CloudWatch log group to which CloudFormation sends error logging information when invoking the type's handlers.
        /// </summary>
        [Input("logGroupName")]
        public Input<string>? LogGroupName { get; set; }

        /// <summary>
        /// The ARN of the role that CloudFormation should assume when sending log entries to CloudWatch logs.
        /// </summary>
        [Input("logRoleArn")]
        public Input<string>? LogRoleArn { get; set; }

        public ResourceVersionLoggingConfigArgs()
        {
        }
        public static new ResourceVersionLoggingConfigArgs Empty => new ResourceVersionLoggingConfigArgs();
    }
}
