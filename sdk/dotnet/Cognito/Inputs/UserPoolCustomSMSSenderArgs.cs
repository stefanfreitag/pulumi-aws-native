// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Cognito.Inputs
{

    public sealed class UserPoolCustomSMSSenderArgs : Pulumi.ResourceArgs
    {
        [Input("lambdaArn")]
        public Input<string>? LambdaArn { get; set; }

        [Input("lambdaVersion")]
        public Input<string>? LambdaVersion { get; set; }

        public UserPoolCustomSMSSenderArgs()
        {
        }
    }
}
