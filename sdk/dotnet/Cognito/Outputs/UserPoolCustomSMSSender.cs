// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Cognito.Outputs
{

    [OutputType]
    public sealed class UserPoolCustomSMSSender
    {
        public readonly string? LambdaArn;
        public readonly string? LambdaVersion;

        [OutputConstructor]
        private UserPoolCustomSMSSender(
            string? lambdaArn,

            string? lambdaVersion)
        {
            LambdaArn = lambdaArn;
            LambdaVersion = lambdaVersion;
        }
    }
}
