// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.RoboMaker.Outputs
{

    [OutputType]
    public sealed class RobotApplicationRobotSoftwareSuite
    {
        public readonly string Name;
        public readonly string Version;

        [OutputConstructor]
        private RobotApplicationRobotSoftwareSuite(
            string name,

            string version)
        {
            Name = name;
            Version = version;
        }
    }
}
