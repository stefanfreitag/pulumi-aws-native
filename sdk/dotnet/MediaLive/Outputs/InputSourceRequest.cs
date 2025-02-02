// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MediaLive.Outputs
{

    [OutputType]
    public sealed class InputSourceRequest
    {
        public readonly string? PasswordParam;
        public readonly string? Url;
        public readonly string? Username;

        [OutputConstructor]
        private InputSourceRequest(
            string? passwordParam,

            string? url,

            string? username)
        {
            PasswordParam = passwordParam;
            Url = url;
            Username = username;
        }
    }
}
