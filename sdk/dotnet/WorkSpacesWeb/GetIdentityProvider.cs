// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WorkSpacesWeb
{
    public static class GetIdentityProvider
    {
        /// <summary>
        /// Definition of AWS::WorkSpacesWeb::IdentityProvider Resource Type
        /// </summary>
        public static Task<GetIdentityProviderResult> InvokeAsync(GetIdentityProviderArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetIdentityProviderResult>("aws-native:workspacesweb:getIdentityProvider", args ?? new GetIdentityProviderArgs(), options.WithDefaults());

        /// <summary>
        /// Definition of AWS::WorkSpacesWeb::IdentityProvider Resource Type
        /// </summary>
        public static Output<GetIdentityProviderResult> Invoke(GetIdentityProviderInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetIdentityProviderResult>("aws-native:workspacesweb:getIdentityProvider", args ?? new GetIdentityProviderInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetIdentityProviderArgs : global::Pulumi.InvokeArgs
    {
        [Input("identityProviderArn", required: true)]
        public string IdentityProviderArn { get; set; } = null!;

        public GetIdentityProviderArgs()
        {
        }
        public static new GetIdentityProviderArgs Empty => new GetIdentityProviderArgs();
    }

    public sealed class GetIdentityProviderInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("identityProviderArn", required: true)]
        public Input<string> IdentityProviderArn { get; set; } = null!;

        public GetIdentityProviderInvokeArgs()
        {
        }
        public static new GetIdentityProviderInvokeArgs Empty => new GetIdentityProviderInvokeArgs();
    }


    [OutputType]
    public sealed class GetIdentityProviderResult
    {
        public readonly string? IdentityProviderArn;
        public readonly Outputs.IdentityProviderDetails? IdentityProviderDetails;
        public readonly string? IdentityProviderName;
        public readonly Pulumi.AwsNative.WorkSpacesWeb.IdentityProviderType? IdentityProviderType;

        [OutputConstructor]
        private GetIdentityProviderResult(
            string? identityProviderArn,

            Outputs.IdentityProviderDetails? identityProviderDetails,

            string? identityProviderName,

            Pulumi.AwsNative.WorkSpacesWeb.IdentityProviderType? identityProviderType)
        {
            IdentityProviderArn = identityProviderArn;
            IdentityProviderDetails = identityProviderDetails;
            IdentityProviderName = identityProviderName;
            IdentityProviderType = identityProviderType;
        }
    }
}
