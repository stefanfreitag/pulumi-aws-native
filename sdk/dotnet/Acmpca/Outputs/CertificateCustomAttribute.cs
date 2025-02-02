// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Acmpca.Outputs
{

    [OutputType]
    public sealed class CertificateCustomAttribute
    {
        public readonly string ObjectIdentifier;
        public readonly string Value;

        [OutputConstructor]
        private CertificateCustomAttribute(
            string objectIdentifier,

            string value)
        {
            ObjectIdentifier = objectIdentifier;
            Value = value;
        }
    }
}
