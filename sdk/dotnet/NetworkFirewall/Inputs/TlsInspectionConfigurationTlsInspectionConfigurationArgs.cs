// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.NetworkFirewall.Inputs
{

    public sealed class TlsInspectionConfigurationTlsInspectionConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("serverCertificateConfigurations")]
        private InputList<Inputs.TlsInspectionConfigurationServerCertificateConfigurationArgs>? _serverCertificateConfigurations;
        public InputList<Inputs.TlsInspectionConfigurationServerCertificateConfigurationArgs> ServerCertificateConfigurations
        {
            get => _serverCertificateConfigurations ?? (_serverCertificateConfigurations = new InputList<Inputs.TlsInspectionConfigurationServerCertificateConfigurationArgs>());
            set => _serverCertificateConfigurations = value;
        }

        public TlsInspectionConfigurationTlsInspectionConfigurationArgs()
        {
        }
        public static new TlsInspectionConfigurationTlsInspectionConfigurationArgs Empty => new TlsInspectionConfigurationTlsInspectionConfigurationArgs();
    }
}
