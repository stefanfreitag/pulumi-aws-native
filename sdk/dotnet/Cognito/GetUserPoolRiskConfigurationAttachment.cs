// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Cognito
{
    public static class GetUserPoolRiskConfigurationAttachment
    {
        /// <summary>
        /// Resource Type definition for AWS::Cognito::UserPoolRiskConfigurationAttachment
        /// </summary>
        public static Task<GetUserPoolRiskConfigurationAttachmentResult> InvokeAsync(GetUserPoolRiskConfigurationAttachmentArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetUserPoolRiskConfigurationAttachmentResult>("aws-native:cognito:getUserPoolRiskConfigurationAttachment", args ?? new GetUserPoolRiskConfigurationAttachmentArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::Cognito::UserPoolRiskConfigurationAttachment
        /// </summary>
        public static Output<GetUserPoolRiskConfigurationAttachmentResult> Invoke(GetUserPoolRiskConfigurationAttachmentInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetUserPoolRiskConfigurationAttachmentResult>("aws-native:cognito:getUserPoolRiskConfigurationAttachment", args ?? new GetUserPoolRiskConfigurationAttachmentInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetUserPoolRiskConfigurationAttachmentArgs : global::Pulumi.InvokeArgs
    {
        [Input("clientId", required: true)]
        public string ClientId { get; set; } = null!;

        [Input("userPoolId", required: true)]
        public string UserPoolId { get; set; } = null!;

        public GetUserPoolRiskConfigurationAttachmentArgs()
        {
        }
        public static new GetUserPoolRiskConfigurationAttachmentArgs Empty => new GetUserPoolRiskConfigurationAttachmentArgs();
    }

    public sealed class GetUserPoolRiskConfigurationAttachmentInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("clientId", required: true)]
        public Input<string> ClientId { get; set; } = null!;

        [Input("userPoolId", required: true)]
        public Input<string> UserPoolId { get; set; } = null!;

        public GetUserPoolRiskConfigurationAttachmentInvokeArgs()
        {
        }
        public static new GetUserPoolRiskConfigurationAttachmentInvokeArgs Empty => new GetUserPoolRiskConfigurationAttachmentInvokeArgs();
    }


    [OutputType]
    public sealed class GetUserPoolRiskConfigurationAttachmentResult
    {
        public readonly Outputs.UserPoolRiskConfigurationAttachmentAccountTakeoverRiskConfigurationType? AccountTakeoverRiskConfiguration;
        public readonly Outputs.UserPoolRiskConfigurationAttachmentCompromisedCredentialsRiskConfigurationType? CompromisedCredentialsRiskConfiguration;
        public readonly Outputs.UserPoolRiskConfigurationAttachmentRiskExceptionConfigurationType? RiskExceptionConfiguration;

        [OutputConstructor]
        private GetUserPoolRiskConfigurationAttachmentResult(
            Outputs.UserPoolRiskConfigurationAttachmentAccountTakeoverRiskConfigurationType? accountTakeoverRiskConfiguration,

            Outputs.UserPoolRiskConfigurationAttachmentCompromisedCredentialsRiskConfigurationType? compromisedCredentialsRiskConfiguration,

            Outputs.UserPoolRiskConfigurationAttachmentRiskExceptionConfigurationType? riskExceptionConfiguration)
        {
            AccountTakeoverRiskConfiguration = accountTakeoverRiskConfiguration;
            CompromisedCredentialsRiskConfiguration = compromisedCredentialsRiskConfiguration;
            RiskExceptionConfiguration = riskExceptionConfiguration;
        }
    }
}
