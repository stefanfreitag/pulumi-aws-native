// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WorkSpacesWeb
{
    public static class GetPortal
    {
        /// <summary>
        /// Definition of AWS::WorkSpacesWeb::Portal Resource Type
        /// </summary>
        public static Task<GetPortalResult> InvokeAsync(GetPortalArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetPortalResult>("aws-native:workspacesweb:getPortal", args ?? new GetPortalArgs(), options.WithDefaults());

        /// <summary>
        /// Definition of AWS::WorkSpacesWeb::Portal Resource Type
        /// </summary>
        public static Output<GetPortalResult> Invoke(GetPortalInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetPortalResult>("aws-native:workspacesweb:getPortal", args ?? new GetPortalInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetPortalArgs : global::Pulumi.InvokeArgs
    {
        [Input("portalArn", required: true)]
        public string PortalArn { get; set; } = null!;

        public GetPortalArgs()
        {
        }
        public static new GetPortalArgs Empty => new GetPortalArgs();
    }

    public sealed class GetPortalInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("portalArn", required: true)]
        public Input<string> PortalArn { get; set; } = null!;

        public GetPortalInvokeArgs()
        {
        }
        public static new GetPortalInvokeArgs Empty => new GetPortalInvokeArgs();
    }


    [OutputType]
    public sealed class GetPortalResult
    {
        public readonly Pulumi.AwsNative.WorkSpacesWeb.PortalAuthenticationType? AuthenticationType;
        public readonly string? BrowserSettingsArn;
        public readonly Pulumi.AwsNative.WorkSpacesWeb.PortalBrowserType? BrowserType;
        public readonly string? CreationDate;
        public readonly string? DisplayName;
        public readonly string? IpAccessSettingsArn;
        public readonly string? NetworkSettingsArn;
        public readonly string? PortalArn;
        public readonly string? PortalEndpoint;
        public readonly Pulumi.AwsNative.WorkSpacesWeb.PortalStatus? PortalStatus;
        public readonly Pulumi.AwsNative.WorkSpacesWeb.PortalRendererType? RendererType;
        public readonly string? ServiceProviderSamlMetadata;
        public readonly string? StatusReason;
        public readonly ImmutableArray<Outputs.PortalTag> Tags;
        public readonly string? TrustStoreArn;
        public readonly string? UserAccessLoggingSettingsArn;
        public readonly string? UserSettingsArn;

        [OutputConstructor]
        private GetPortalResult(
            Pulumi.AwsNative.WorkSpacesWeb.PortalAuthenticationType? authenticationType,

            string? browserSettingsArn,

            Pulumi.AwsNative.WorkSpacesWeb.PortalBrowserType? browserType,

            string? creationDate,

            string? displayName,

            string? ipAccessSettingsArn,

            string? networkSettingsArn,

            string? portalArn,

            string? portalEndpoint,

            Pulumi.AwsNative.WorkSpacesWeb.PortalStatus? portalStatus,

            Pulumi.AwsNative.WorkSpacesWeb.PortalRendererType? rendererType,

            string? serviceProviderSamlMetadata,

            string? statusReason,

            ImmutableArray<Outputs.PortalTag> tags,

            string? trustStoreArn,

            string? userAccessLoggingSettingsArn,

            string? userSettingsArn)
        {
            AuthenticationType = authenticationType;
            BrowserSettingsArn = browserSettingsArn;
            BrowserType = browserType;
            CreationDate = creationDate;
            DisplayName = displayName;
            IpAccessSettingsArn = ipAccessSettingsArn;
            NetworkSettingsArn = networkSettingsArn;
            PortalArn = portalArn;
            PortalEndpoint = portalEndpoint;
            PortalStatus = portalStatus;
            RendererType = rendererType;
            ServiceProviderSamlMetadata = serviceProviderSamlMetadata;
            StatusReason = statusReason;
            Tags = tags;
            TrustStoreArn = trustStoreArn;
            UserAccessLoggingSettingsArn = userAccessLoggingSettingsArn;
            UserSettingsArn = userSettingsArn;
        }
    }
}
