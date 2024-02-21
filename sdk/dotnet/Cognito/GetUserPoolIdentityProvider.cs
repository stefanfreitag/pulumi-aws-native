// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Cognito
{
    public static class GetUserPoolIdentityProvider
    {
        /// <summary>
        /// Resource Type definition for AWS::Cognito::UserPoolIdentityProvider
        /// </summary>
        public static Task<GetUserPoolIdentityProviderResult> InvokeAsync(GetUserPoolIdentityProviderArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetUserPoolIdentityProviderResult>("aws-native:cognito:getUserPoolIdentityProvider", args ?? new GetUserPoolIdentityProviderArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::Cognito::UserPoolIdentityProvider
        /// </summary>
        public static Output<GetUserPoolIdentityProviderResult> Invoke(GetUserPoolIdentityProviderInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetUserPoolIdentityProviderResult>("aws-native:cognito:getUserPoolIdentityProvider", args ?? new GetUserPoolIdentityProviderInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetUserPoolIdentityProviderArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetUserPoolIdentityProviderArgs()
        {
        }
        public static new GetUserPoolIdentityProviderArgs Empty => new GetUserPoolIdentityProviderArgs();
    }

    public sealed class GetUserPoolIdentityProviderInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetUserPoolIdentityProviderInvokeArgs()
        {
        }
        public static new GetUserPoolIdentityProviderInvokeArgs Empty => new GetUserPoolIdentityProviderInvokeArgs();
    }


    [OutputType]
    public sealed class GetUserPoolIdentityProviderResult
    {
        /// <summary>
        /// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Cognito::UserPoolIdentityProvider` for more information about the expected schema for this property.
        /// </summary>
        public readonly object? AttributeMapping;
        public readonly string? Id;
        public readonly ImmutableArray<string> IdpIdentifiers;
        /// <summary>
        /// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Cognito::UserPoolIdentityProvider` for more information about the expected schema for this property.
        /// </summary>
        public readonly object? ProviderDetails;

        [OutputConstructor]
        private GetUserPoolIdentityProviderResult(
            object? attributeMapping,

            string? id,

            ImmutableArray<string> idpIdentifiers,

            object? providerDetails)
        {
            AttributeMapping = attributeMapping;
            Id = id;
            IdpIdentifiers = idpIdentifiers;
            ProviderDetails = providerDetails;
        }
    }
}
