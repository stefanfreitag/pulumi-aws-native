// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Acmpca.Outputs
{

    /// <summary>
    /// Contains information about the certificate subject. The Subject field in the certificate identifies the entity that owns or controls the public key in the certificate. The entity can be a user, computer, device, or service. The Subject must contain an X.500 distinguished name (DN). A DN is a sequence of relative distinguished names (RDNs). The RDNs are separated by commas in the certificate.
    /// </summary>
    [OutputType]
    public sealed class CertificateApiPassthrough
    {
        public readonly Outputs.CertificateExtensions? Extensions;
        /// <summary>
        /// Contains information about the certificate subject. The Subject field in the certificate identifies the entity that owns or controls the public key in the certificate. The entity can be a user, computer, device, or service. The Subject must contain an X.500 distinguished name (DN). A DN is a sequence of relative distinguished names (RDNs). The RDNs are separated by commas in the certificate.
        /// </summary>
        public readonly Outputs.CertificateSubject? Subject;

        [OutputConstructor]
        private CertificateApiPassthrough(
            Outputs.CertificateExtensions? extensions,

            Outputs.CertificateSubject? subject)
        {
            Extensions = extensions;
            Subject = subject;
        }
    }
}
