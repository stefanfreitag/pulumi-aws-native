// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Cognito.Inputs
{

    public sealed class UserPoolStringAttributeConstraintsArgs : global::Pulumi.ResourceArgs
    {
        [Input("maxLength")]
        public Input<string>? MaxLength { get; set; }

        [Input("minLength")]
        public Input<string>? MinLength { get; set; }

        public UserPoolStringAttributeConstraintsArgs()
        {
        }
        public static new UserPoolStringAttributeConstraintsArgs Empty => new UserPoolStringAttributeConstraintsArgs();
    }
}
