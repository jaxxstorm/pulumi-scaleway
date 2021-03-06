// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Scaleway
{
    public static class GetVolume
    {
        /// <summary>
        /// Gets information about a Volume.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Scaleway = Pulumi.Scaleway;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var dataVolume = Output.Create(Scaleway.GetVolume.InvokeAsync(new Scaleway.GetVolumeArgs
        ///         {
        ///             Name = "data",
        ///         }));
        ///         var test = new Scaleway.Server("test", new Scaleway.ServerArgs
        ///         {
        ///         });
        ///         // ...
        ///         var dataVolumeAttachment = new Scaleway.VolumeAttachment("dataVolumeAttachment", new Scaleway.VolumeAttachmentArgs
        ///         {
        ///             Server = test.Id,
        ///             Volume = scaleway_volume.Data.Id,
        ///         });
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetVolumeResult> InvokeAsync(GetVolumeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetVolumeResult>("scaleway:index/getVolume:getVolume", args ?? new GetVolumeArgs(), options.WithVersion());
    }


    public sealed class GetVolumeArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Exact name of the Volume.
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        public GetVolumeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetVolumeResult
    {
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string Name;
        /// <summary>
        /// The ID of the Server which this Volume is currently attached to.
        /// </summary>
        public readonly string Server;
        /// <summary>
        /// (Required) size of the volume in GB
        /// </summary>
        public readonly int SizeInGb;
        /// <summary>
        /// The type of volume this is, such as `l_ssd`.
        /// </summary>
        public readonly string Type;

        [OutputConstructor]
        private GetVolumeResult(
            string id,

            string name,

            string server,

            int sizeInGb,

            string type)
        {
            Id = id;
            Name = name;
            Server = server;
            SizeInGb = sizeInGb;
            Type = type;
        }
    }
}
