// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SageMaker.Inputs
{

    public sealed class WorkteamCognitoMemberDefinitionArgs : global::Pulumi.ResourceArgs
    {
        [Input("cognitoClientId", required: true)]
        public Input<string> CognitoClientId { get; set; } = null!;

        [Input("cognitoUserGroup", required: true)]
        public Input<string> CognitoUserGroup { get; set; } = null!;

        [Input("cognitoUserPool", required: true)]
        public Input<string> CognitoUserPool { get; set; } = null!;

        public WorkteamCognitoMemberDefinitionArgs()
        {
        }
        public static new WorkteamCognitoMemberDefinitionArgs Empty => new WorkteamCognitoMemberDefinitionArgs();
    }
}
